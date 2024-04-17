from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events
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
            if form.is_valid():
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
        items = Events.objects.all()
        context = {
            'items':items,
        }
        return render(response, "main/eventslist.html",context)
    else:
        return HttpResponseRedirect("/info/")

def index(response,id):
    if response.user.is_authenticated:
        item = Events.objects.get(id=id)
        return render(response,'main/index.html',{'item':item})
    else:
        return HttpResponseRedirect("/info/")

def mylist(request):
    if request.user.is_authenticated:
        username = request.user.username
        items = Events.objects.filter(user__username = username)
        return render(request,'main/mylist.html',{'items':items})
    else:
        return HttpResponseRedirect("/info/")

def deleteEvent(request,id):
    if request.user.is_authenticated:
        Events.objects.get(id=id).delete()
        return HttpResponseRedirect("/mylist/")
    else:
        return HttpResponseRedirect("/info/")

