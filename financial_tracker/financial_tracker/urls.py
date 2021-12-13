from django import contrib
from django.contrib import admin
from django.urls import path, include
from register import views as register_view
from home import views as home_view
from tracker import views as tracker_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view.home, name="welcome"),
    path("signup/", register_view.registerUser, name="signup"),
    # login path is already pre-defined by django so no need to define it
    path("", include("django.contrib.auth.urls")),
    # the page displayed when user logs in
    path("userhome/<int:id>", tracker_view.save_user_tracker_items, name="trackerpage"),
    path("createtracker/<int:id>", tracker_view.create_tracker, name="create"),
    path(
        "deleteitems/<items_id>",
        tracker_view.delete_tracker_items,
        name="delete-tracker-item",
    ),
    path("edititems/<items_id>", tracker_view.edit_items, name="edit-tracker-items"),
    path("trackerviews/", tracker_view.view_trackers, name="view"),
]
