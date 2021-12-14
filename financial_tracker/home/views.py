from django.shortcuts import render

# the home page
def home(request):
    return render(request, "homePage/index.html", {})
