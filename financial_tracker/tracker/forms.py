from django import forms


class CreateNewTrackerForm(forms.Form):
    """Create new tracker form"""
    name = forms.CharField(label="Name", max_length=200)