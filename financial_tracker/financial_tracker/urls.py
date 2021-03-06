from django import contrib
from django.contrib import admin
from django.urls import path, include
from register import views as register_view
from home import views as home_view
from tracker import views as tracker_view

urlpatterns = [
    path("admin/", admin.site.urls),

    # home page url
    path("", home_view.home, name="welcome"),

    # sign up page url
    path("signup/", register_view.registerUser, name="signup"),

    # login path is already pre-defined by django so no need to define it
    path("", include("django.contrib.auth.urls")),

    # the page displayed when user logs in
    # this is where you add the payments to the tracker
    path("userhome/<int:id>", tracker_view.save_user_tracker_items, name="trackerpage"),

    # the create tracker page
    path("createtracker/<int:id>", tracker_view.create_tracker, name="create"),

    # the deleteitems url which is executed by the delete function
    path(
        "deleteitems/<items_id>",
        tracker_view.delete_tracker_items,
        name="delete-tracker-item",
    ),

    # the url to edit items in the tracker
    path("edititems/<items_id>", tracker_view.edit_items, name="edit-tracker-items"),

    # the page to view the tracker information
    path("trackerviews/", tracker_view.view_trackers, name="view"),
]
