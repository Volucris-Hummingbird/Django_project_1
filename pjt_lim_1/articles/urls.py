from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path("", views.articles, name="articles"),

    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),


    path("index/", views.index),
    path("users/", views.users),
    path("datathrow/", views.datathrow),
    path("datacatch/", views.datacatch),
]
