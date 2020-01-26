from django.shortcuts import render, HttpResponseRedirect
from common import game, some_func
import os

# Create your views here.
def save_f(request):
    s = game.slot()
    d = game.data_game()
    d.load_state()
    slots = some_func.get_slots("save_files")
    if request.method == "POST":
        if 'up' in request.POST:
            s.minus()
        elif 'down' in request.POST:
            s.plus()
        return HttpResponseRedirect(request.path)
    

    return render(request, "save.html", {"slot_place":s.slot_place, "slotA":slots['A'] , "slotB":slots['B'] , "slotC":slots['C']  })