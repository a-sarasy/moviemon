from django.shortcuts import render
from django.conf import settings

# Create your views here.

def wordmap_f(request):
    return render(
                request, 
                "worldmap.html", {
                    'mapx': range(settings.GRID_SIZE),
                    'mapy': range(settings.GRID_SIZE),
                    'persox': 0,
                    'persoy': 1,
                    'balls_number': 7,
                    'ballfindstring': "You encountered Shining",
                    'moviefindstring': 'You just found a ball!'
                    }
    )
