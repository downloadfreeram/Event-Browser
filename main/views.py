from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events, EventParticipation, EventComments
from .forms import CreateNewEvent, CreateEventComments
from django.db.models import Q
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(response):
    '''
    Function for home page 
    '''
    return render(
        response,
        "main/home.html",
        {})

def info(response):
    '''
    Function for info site which contains a message about only using website when the user has
    an account
    '''
    return render(response,
                  "main/info.html",
                  {})

def site(response):
    '''
    Function for site page
    '''
    if response.user.is_authenticated:
        return render(response,
                      "main/site.html",
                      {})
    else:
        return HttpResponseRedirect("/info/")

def create(response):
    '''
    Function to create an event by a user, after checking if POST is successful,
    retrieve the data from form and insert it into the database
    '''
    if response.user.is_authenticated:
        if response.method == "POST":
            form = CreateNewEvent(response.POST or None)
            #check if the form has data in it
            if form.is_valid():
                #process the post data and add it to the db
                d = form.cleaned_data["name"]
                des = form.cleaned_data["description"]
                dat = form.cleaned_data["date"]
                cou = form.cleaned_data["country"]
                city = form.cleaned_data["city"]
                t = Events(name=d,
                           date=dat,
                           description=des
                           ,country=cou,
                           city=city)
                t.save()
                response.user.event.add(t)

                return HttpResponseRedirect("/eventslist/")
            else:
                form = CreateNewEvent()
                print("not valid")
        else:
            form = CreateNewEvent()
        return render(response,
                      "main/create.html",
                      {'form':form})
    else:
        return HttpResponseRedirect("/info/")

def signout(response):
    '''
    Function to handle signing out the user
    '''
    return render(response, "main/signout.html", {})

def eventslist(response):
    '''
    Site used to gather all currently created events, using the objects.all() method on the 
    Events model, and also using the searchbar to search for events
    '''
    if response.user.is_authenticated:
        #get all of the event data to render it on the webpage
        items = Events.objects.all()
        #filter by name in search bar
        search = response.GET.get('searchBar')
        if search != '' and search is not None:
            items = items.filter(name__icontains = search)
        context = {
            'items':items,
        }
        return render(
            response,
            "main/eventslist.html",
            context)
    else:
        return HttpResponseRedirect("/info/")

def index(response,id):
    '''
    Site used to show a specific event, it is done by getting an id of an event and 
    using a query to filter every field that is related to the id of an event,
    this function is also handling the user's will to participate in an event that 
    will show in the designated spot in the app, it is done by adding a new entry to
    the EventParticipation database that has the info of specific user and the id of
    event that he wants to participate in, the last thing that the function does is 
    handling the comments for specific event, which is also done by using a new database
    and adding the comment to this database, which is then showed in the bottom section
    '''
    if response.user.is_authenticated:
        #get an id of user's event to use it as a website
        item = Events.objects.get(id=id) 
        usr = response.user.username
        comments = EventComments.objects.filter(eventId = id).order_by('commentData')
        #check which POST has been clicked
        if response.method == "POST" and "btnParticipate" in response.POST:
            #using Q objects for queries, check if the user is curently participating in the event, if yes then show the alert message
            if(EventParticipation.objects.filter(Q(user = usr)&Q(eventId = id))):
                messages.add_message(
                    response, 
                    messages.INFO,
                    "You are currently participating in the event")
            else:
                query = EventParticipation(user=usr,
                                            eventId=id,
                                            name=item.name,
                                            date=item.date,
                                            participation="yes")
                query.save()
                return HttpResponseRedirect("/site/")
        if response.method == "POST" and "btnComment" in response.POST:
            form_text = response.POST.get("text")
            query = EventComments(user = usr, eventId = id, text = form_text)
            query.save()
            return HttpResponseRedirect("")
        else:
            print("POST failed")
        context = {
            'item':item,
            'comments':comments,
        }
        return render(response,'main/index.html',context)
    else:
        return HttpResponseRedirect("/info/")

def mylist(request):
    '''
    Site that gathers the info about user created events and the events that the user 
    wants to participate in, done by filtering by username
    '''
    if request.user.is_authenticated:
        #request user's name and then create a query in the Events db
        username = request.user.username
        items = Events.objects.filter(user__username = username)
        events_items = EventParticipation.objects.filter(user = username)
        return render(request,
                      'main/mylist.html',
                      {'items':items,
                       'events_items':events_items})
    else:
        return HttpResponseRedirect("/info/")

def deleteEvent(request,id):
    '''
    Function used to delete a created event, not only does the function removes entirety
    of an Event but also it removes the comments on it and the will of participation of 
    the users, by using the Q query to delete by specific event Id
    '''
    if request.user.is_authenticated:
        username = request.user.username
        #delete user's event with query to delete by specific event id
        Events.objects.get(id=id).delete()
        #also delete all instances of events
        EventParticipation.objects.filter(Q(eventId=id)).delete()
        EventComments.objects.filter(Q(eventId=id)).delete()
        return HttpResponseRedirect("/mylist/")
    else:
        return HttpResponseRedirect("/info/")

def participate(request,id):
    '''
    Function handling the participation action
    '''
    if request.user.is_authenticated:
        if request.method == "POST":
            return render(request,'main/site.html',{})
    else:
        return HttpResponseRedirect("/info/")
