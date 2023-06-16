from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path("login/", views.login),
    path(' ', views.dash),
     path("dashboard/", views.dash),
]
