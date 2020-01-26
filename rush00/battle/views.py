from django.shortcuts import render, Http404
from common import game

# Create your views here.
def battle_f(request, moviemon_id):
    d = game.data_game()
    d.load_state()
    movie = d.get_movie(moviemon_id)
    player_strength = d.get_strength()
    success_proba = 50 - (float(movie['rating']) * 10) + (player_strength * 5)
    if success_proba < 1:
        success_proba = 1
    elif success_proba > 90:
        success_proba = 90
    # mettre un get ici pour avoir les parametres du combat
    captured = False
    missed = True
    if d.capturable == moviemon_id:
        return render(request, "battle.html", {
            'poster': movie['poster'],
            'balls_number': d.data['nbr_movieball'],
            'player_strength': player_strength,
            'success_proba': success_proba,
            'captured': captured,
            'missed': missed,
            'movieball_tosslink': 'http://127.0.0.1:8000/tossball/',
            'moviemon_strength': movie['rating']
            })
    else:
        raise Http404()