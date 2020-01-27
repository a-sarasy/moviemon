from django.shortcuts import render, HttpResponseRedirect
from common import game, some_func
from django.conf import settings

# Create your views here.
def load_f(request):
    s = game.slot()
    d = game.data_game()
    a_link =  "http://127.0.0.1:8000/options/load_game/?slot={}".format(s.slot_place)
    slots = some_func.get_slots(settings.SAVE_FILES)
    slots_name = some_func.get_val_slots(settings.SAVE_FILES)
    a_text = "A - Load"
    if slots_name[list(['a','b','c'])[s.slot_place]] == None:
        a_link = '#'
    if request.method == "POST":
        if 'up' in request.POST:
            s.minus()
        elif 'down' in request.POST:
            s.plus()
        return HttpResponseRedirect(request.path)
    if request.method == "GET":
        if 'slot' in request.GET and not slots_name[list(['a','b','c'])[s.slot_place]] == None:    
            d.load_game(slots_name[list(['a','b','c'])[s.slot_place]])
            a_link = "http://127.0.0.1:8000/worldmap"
            a_text = "A - START GAME"


    return render(request, "load.html", {"slot_place":s.slot_place, "slotA":slots['a'] , "slotB":slots['b'] , "slotC":slots['c'],"load_link":a_link,"worldmap_link":"http://127.0.0.1:8000/",'a_text':a_text  })