from django.shortcuts import render


def tracker(request):
    return render(request, "tracker/user-tracker.html", {})