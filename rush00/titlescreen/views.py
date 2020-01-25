from django.shortcuts import render, HttpResponse
import requests
from common import movies

# Create your views here.


def titlescreen_f(request):
    movies_obj = movies.Movies_info()
    movies_info_list = movies_obj.get_list()
    # print(movies_info_list)
    return render(request, "titlescreen/titlescreen.html", {"name": "worldmap"})
