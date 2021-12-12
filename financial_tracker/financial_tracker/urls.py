"""financial_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import contrib
from django.contrib import admin
from django.urls import path, include
from register import views as register_view
from home import views as home_view
from tracker import views as tracker_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.home, name="welcome"), 
    path("signup/", register_view.registerUser, name="signup"),

    # login path is already pre-defined by django so no need to define it 
    path('', include('django.contrib.auth.urls')),
    
    # the page displayed when user logs in
    path('userhome/<int:id>',tracker_view.save_user_tracker_items, name="trackerpage"),
    path('createtracker/<int:id>',tracker_view.create_tracker, name="create"),
    path('trackerviews/',tracker_view.view_trackers, name="view"),

]
