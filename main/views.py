from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events, EventParticipation
from .forms import CreateNewEvent

# Create your views here.
def home(response):
    return render(response, "main/home.html",{})

def info(response):
    return render(response,"main/info.html",{})

def site(response):
    if response.user.is_authenticated:
        print("authenticated")
        return render(response, "main/site.html", {})
    else:
        return HttpResponseRedirect("/info/")

def create(response):
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
                t = Events(name=d,date=dat,description=des,country=cou,city=city)
                t.save()
                response.user.event.add(t)

                return HttpResponseRedirect("/eventslist/")
            else:
                form = CreateNewEvent()
                print("not valid")
        else:
            form = CreateNewEvent()
        return render(response, "main/create.html",{'form':form})
    else:
        return HttpResponseRedirect("/info/")

def signout(response):
    return render(response, "main/signout.html", {})

def eventslist(response):
    if response.user.is_authenticated:
        #get all of the event data to render it on the webpage
        items = Events.objects.all()
        context = {
            'items':items,
        }
        return render(response, "main/eventslist.html",context)
    else:
        return HttpResponseRedirect("/info/")

def index(response,id):
    if response.user.is_authenticated:
        #get an id of user's event to use it as a website
        item = Events.objects.get(id=id)
        #after pressing the "participate" submit button add a new entry to the EventParticipation database about user's action
        if response.method == "POST":
            print("post succesfully done")
            usr = response.user.username
            query = EventParticipation(user=usr,eventId=id,participation="yes")
            query.save()
            return HttpResponseRedirect("/site/")
        else:
            print("post failed")
        return render(response,'main/index.html',{'item':item})
    else:
        return HttpResponseRedirect("/info/")

def mylist(request):
    if request.user.is_authenticated:
        #request user's name and then create a query in the Events db
        username = request.user.username
        items = Events.objects.filter(user__username = username)
        return render(request,'main/mylist.html',{'items':items})
    else:
        return HttpResponseRedirect("/info/")

def deleteEvent(request,id):
    if request.user.is_authenticated:
        #delete user's event with query to delete by specific event id
        Events.objects.get(id=id).delete()
        return HttpResponseRedirect("/mylist/")
    else:
        return HttpResponseRedirect("/info/")

def participate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            print("dziala")
            return render(request,'main/site.html',{})
    else:
        return HttpResponseRedirect("/info/")