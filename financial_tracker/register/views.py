from django.shortcuts import render, redirect
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext


def home(request):
    return render(request, "index.html", {})

def registerUser(response):
    # if there is a post request and form is valid
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            # save the form
            form.save()

        return(redirect(''))
    else:
        #otherwise create a blank form
        form = UserCreationForm()

    return render(response, "register/signup.html", {"form":form}, )
    