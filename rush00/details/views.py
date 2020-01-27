from django.shortcuts import render, Http404
from common import game

# Create your views here.
def details_f(request, moviemon_id):
    d = game.data_game()
    d.load_state()
    #search for the moviemon in the total list.
    movie = d.get_movie(moviemon_id)
    if movie is not None:
        return render(request, "details.html", {'movie': movie})
    #If the moviemon is not found, raise 404.
    raise Http404()