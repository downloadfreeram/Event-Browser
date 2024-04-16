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
            d = form.cleaned_data
            t = CreateNewEvent(d)
            t.save()
            return HttpResponseRedirect("/site/")
        else:
            form = CreateNewEvent()
            print("not valid")
    else:
        form = CreateNewEvent()
    return render(response, "main/create.html",{'form':form})

def signout(response):
    return render(response, "main/signout.html", {})