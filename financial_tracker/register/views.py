from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from . forms import RegistrationForm


def home(request):
    return render(request, "index.html", {})

def registerUser(response):
    # if there is a post request and form is valid
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            # save the form
            form.save()

        # return(redirect(''))
    else:
        #otherwise create a blank form
        form = RegistrationForm()

    return render(response, "register/signup.html", {"form":form}, )
    