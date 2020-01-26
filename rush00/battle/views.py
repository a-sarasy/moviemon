from django.shortcuts import render, HttpResponse

# Create your views here.
def battle_f(request, moviemon):
    return HttpResponse(moviemon)
    