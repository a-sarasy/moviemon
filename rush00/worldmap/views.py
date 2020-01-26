from django.shortcuts import render, HttpResponse, Http404
from django.conf import settings


# Create your views here.

def wordmap_f(request):
    if request.method == "POST":
        if 'up' in request.POST:
            return HttpResponse("Post request received. You want to go up")
        if 'down' in request.POST:
            return HttpResponse("Post request received. You want to go down")
        if 'left' in request.POST:
            return HttpResponse("Post request received. You want to go left")
        if 'right' in request.POST:
            return HttpResponse("Post request received. You want to go right")
        else:
            raise Http404()
    else:
        return render(
                    request, 
                    "worldmap.html", {
                        'mapx': range(settings.GRID_SIZE),
                        'mapy': range(settings.GRID_SIZE),
                        'persox': 0,
                        'persoy': 1,
                        'balls_number': 7,
                        'ballfindstring': "You encountered Shining! Press ? to capture it!",
                        'moviefindstring': 'You just found a ball!'
                        }
        )
