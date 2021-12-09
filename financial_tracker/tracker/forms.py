from django import forms


class CreateNewTracker(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    # check = forms.BooleanField()