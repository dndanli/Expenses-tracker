from django.shortcuts import render
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, "index.html", {})

def registerUser(response):
    form = UserCreationForm()
    return render(response, "register/signup.html", {"form":form})
    