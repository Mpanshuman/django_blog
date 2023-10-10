from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog-home"),
    path("about/", views.about, name="blog-about"),
     path("post/<int:pk>/", views.PostDetailView.as_view(), name="blog-details"),
]
