from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.uploadSpotlight, name="upload"),
    path("queue/", views.spotlightQueue, name="queue"),
    path("edit/<int:id>", views.editSpotlight, name="edit"),
    path("delete/<int:id>", views.deleteSpotlight, name="delete"),
]