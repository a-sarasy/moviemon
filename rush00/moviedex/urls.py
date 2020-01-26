from django.urls import path

from . import views

urlpatterns = [
    path("", views.moviedex_f),
]