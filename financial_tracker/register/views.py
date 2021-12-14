from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect


def registerUser(response):
    """This function register an user"""
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            # save the form
            form.save()

        # redirect user to login page once they're signed-up
        return HttpResponseRedirect("/login/")
    else:
        # otherwise create a blank form
        form = RegistrationForm()

    return render(
        response,
        "register/signup.html",
        {"form": form},
    )
