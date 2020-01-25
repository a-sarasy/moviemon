from django.shortcuts import render
from django.conf import settings

# Create your views here.

def wordmap_f(request):
    return render(request, "worldmap.html", {'mapx': range(settings.GRID_SIZE),'mapy': range(settings.GRID_SIZE)})
