from django.shortcuts import render
from .models import FinancialTracker, TrackerItem

def tracker(request):
    return render(request, "tracker/user-tracker.html", {})

def foo(response, id):
    ft = FinancialTracker.objects.get(id=id)
    return render(response, "tracker/foo.html", {"name":ft.tracker_name})