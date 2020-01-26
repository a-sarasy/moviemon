from django.shortcuts import render, HttpResponse, Http404
from django.conf import settings
from common import game


# Create your views here.

def wordmap_f(request):
    d = game.data_game()
    if request.method == "POST":
        d.load_state()
        if 'up' in request.POST:
            d.data['position'][1] -= 1
        elif 'down' in request.POST:
            d.data['position'][1] += 1
        elif 'left' in request.POST:
            d.data['position'][0] -= 1
        elif 'right' in request.POST:
            d.data['position'][0] += 1
        else:
            raise Http404()
        d.checkpos()
        d.save_state()
    else:
        d.load_default_settings()
        d.save_state()
    return render(
                request, 
                "worldmap.html", {
                    'mapx': range(settings.GRID_SIZE),
                    'mapy': range(settings.GRID_SIZE),
                    'persox': d.data['position'][0],
                    'persoy': d.data['position'][1],
                    'balls_number': d.data['nbr_movieball'],
                    'ballfindstring': "You encountered Shining! Press ? to capture it!",
                    'moviefindstring': 'You just found a ball!'
                    }
    )
