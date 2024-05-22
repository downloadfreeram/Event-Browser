from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()
    email = response.POST.get("email")
    subject = "Welcome!"
    message = "Thanks for registering"
    email_from = settings.EMAIL_HOST_USER
    recipent_list = [email]
    send_mail(subject, message, email_from, recipent_list)
    return render(response, "register/register.html", {"form":form})