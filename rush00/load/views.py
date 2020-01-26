from django.shortcuts import render
from common import game

# Create your views here.
def load_f(request):
    s = game.slot()
    
    if request.method == "POST":
        if 'up' in request.POST:
            s.minus()
        elif 'down' in request.POST:
            s.plus()
    else:
        s.reset()
    return render(request, "load.html", {"slot_place":s.slot_place})