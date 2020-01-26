from django.shortcuts import render, HttpResponseRedirect
from common import game, some_func
from django.conf import settings
import os

# Create your views here.
def save_f(request):
    s = game.slot()
    d = game.data_game()
    d.load_state()
    slots = some_func.get_slots(settings.SAVE_FILES)
    if request.method == "POST":
        if 'up' in request.POST:
            s.minus()
        elif 'down' in request.POST:
            s.plus()
        return HttpResponseRedirect(request.path)
    if request.method == "GET":
        if 'slot' in request.GET:
            d.save_game(s.slot_place)
    

    return render(request, "save.html", {"slot_place":s.slot_place, "slotA":slots['A'] , "slotB":slots['B'] , "slotC":slots['C'], "save_link":"http://127.0.0.1:8000/options/save_game/?slot={}".format(s.slot_place),"worldmap_link":"http://127.0.0.1:8000/worldmap"  })