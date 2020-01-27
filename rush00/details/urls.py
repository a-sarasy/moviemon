from django.urls import path
from . import views

urlpatterns = [
    path("", views.details_f),
]