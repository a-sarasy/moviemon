from django.shortcuts import render
from common import game, some_func

# Create your views here.
def load_f(request):
    s = game.slot()
    
    slots = some_func.get_slots("save_files")
    if request.method == "POST":
        if 'up' in request.POST:
            s.minus()
        elif 'down' in request.POST:
            s.plus()
    else:
        s.reset()

    return render(request, "load.html", {"slot_place":s.slot_place, "slotA":slots['A'] , "slotB":slots['B'] , "slotC":slots['C']  })