from django.shortcuts import render, HttpResponseRedirect
from common import game, some_func
from django.conf import settings

# Create your views here.
def load_f(request):
    s = game.slot()
    d = game.data_game()
    d.load_state()
    a_link =  "http://127.0.0.1:8000/options/load_game/?slot={}".format(s.slot_place)
    slots = some_func.get_slots(settings.SAVE_FILES)
    slots_name = some_func.get_val_slots(settings.SAVE_FILES)
    if slots_name[list(['A','B','C'])[s.slot_place]] == None:
        a_link = '#'
    if request.method == "POST":
        if 'up' in request.POST:
            s.minus()
        elif 'down' in request.POST:
            s.plus()
        return HttpResponseRedirect(request.path)
    if request.method == "GET":
        if 'slot' in request.GET:

            d.load_game(slots_name[list(['A','B','C'])[s.slot_place]])
            a_link = "http://127.0.0.1:8000/worldmap"


    return render(request, "load.html", {"slot_place":s.slot_place, "slotA":slots['A'] , "slotB":slots['B'] , "slotC":slots['C'],"load_link":a_link,"worldmap_link":"http://127.0.0.1:8000/"  })