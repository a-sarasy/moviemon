from django.shortcuts import render, Http404
from common import game

# Create your views here.
def battle_f(request, moviemon_id):
    d = game.data_game()
    print(d.capturable, moviemon_id)
    if d.capturable == moviemon_id:
        return render(request, "battle.html")
    else:
        raise Http404()