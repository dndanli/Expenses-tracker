from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    """This class inherits from the user creation form"""

    email = forms.EmailField()
    # TODO: add date of birth field
    
    class Meta:
        model = User

        # setting the display order of the User fields
        fields = ["username", "email", "password1", "password2"]
        
