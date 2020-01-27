from django.shortcuts import render, HttpResponseRedirect
from common import game, some_func
from django.conf import settings
import os

# Create your views here.
def save_f(request):
    s = game.slot()
    d = game.data_game()
    d.load_state()
    
    if request.method == "POST":
        if 'up' in request.POST:
            s.minus()
        elif 'down' in request.POST:
            s.plus()
        return HttpResponseRedirect(request.path)
    if request.method == "GET":
        if 'slot' in request.GET:
            d.save_game(s.slot_place)
            
    slots = some_func.get_slots(settings.SAVE_FILES)
    

    return render(request, "save.html", {"slot_place":s.slot_place, "slotA":slots['a'] , "slotB":slots['b'] , "slotC":slots['c'], "save_link":"http://127.0.0.1:8000/options/save_game/?slot={}".format(s.slot_place),"options_link":"http://127.0.0.1:8000/options"  })