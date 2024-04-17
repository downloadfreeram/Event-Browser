from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events
from .forms import CreateNewEvent

# Create your views here.
def home(response):
    return render(response, "main/home.html",{})

def site(response):
    return render(response, "main/site.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewEvent(response.POST or None)
        if form.is_valid():
            print("valid")
            d = form.cleaned_data["name"]
            t = Events(name=d)
            t.save()
            response.user.event.add(t)

            return HttpResponseRedirect("/eventslist/")
        else:
            form = CreateNewEvent()
            print("not valid")
    else:
        form = CreateNewEvent()
    return render(response, "main/create.html",{'form':form})

def signout(response):
    return render(response, "main/signout.html", {})

def eventslist(response):
    items = Events.objects.all()
    context = {
        'items':items,
    }
    return render(response, "main/eventslist.html",context)

def index(response,id):
    item = Events.objects.get(id=id)
    return render(response,'main/index.html',{'item':item})

def mylist(request):
    username = request.user.username
    items = Events.objects.filter(user__username = username)
    return render(request,'main/mylist.html',{'items':items})

def deleteEvent(request,id):
    Events.objects.get(id=id).delete()
    return HttpResponseRedirect("/mylist/")
