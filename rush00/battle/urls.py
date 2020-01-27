from django.urls import path

from . import views

urlpatterns = [
    path("<str:moviemon_id>/", views.battle_f),
]
