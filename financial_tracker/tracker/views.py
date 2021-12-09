from django.shortcuts import render
from .models import FinancialTracker, TrackerItem
from .forms import CreateNewTracker

def userTracker(response, id):
    ft = FinancialTracker.objects.get(id=id)
    return render(response, "tracker/user-tracker.html", {"ft":ft})


def create(response):
    # for post methods
    if response.method == "POST":
        form = CreateNewTracker(response.POST)

        if form.is_valid():            
            new_tracker_name = form.cleaned_data["name"]
            new_financial_tracker = FinancialTracker(tracker_name = new_tracker_name)
            new_financial_tracker.save()
    else:
        # if get the just create the new tracker
        form = CreateNewTracker()
        
    return render(response, "tracker/create.html", {"form":form})