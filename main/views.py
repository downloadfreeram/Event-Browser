from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events
from .forms import CreateNewList

# Create your views here.
def home(response):
    return render(response, "main/home.html",{})

def site(response):
    return render(response, "main/site.html", {})

def create(response):
    return render(response, "main/create.html",{})

def signout(response):
    return render(response, "main/signout.html", {})