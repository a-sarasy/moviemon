from django.shortcuts import render, Http404
from common import game
import random

# Create your views here.
def battle_f(request, moviemon_id):
    d = game.data_game()
    d.load_state()
    movie = d.get_movie(moviemon_id)
    player_strength = d.get_strength()
    movieball_link= 'http://127.0.0.1:8000/battle/{}?try_capture=True'.format(moviemon_id)
    success_proba = 50 - (float(movie['rating']) * 10) + (player_strength * 5)
    if success_proba < 1:
        success_proba = 1
    elif success_proba > 90:
        success_proba = 90
    # mettre un get ici pour avoir les parametres du combat
    captured = False
    missed = False
    if request.method == "GET":
        if 'try_capture' in request.GET:
            if d.data['nbr_movieball'] > 0:
                d.data['nbr_movieball'] -= 1
                jet = random.randint(1,100)
                print(jet)
                if int(success_proba) >= jet:
                    captured = True
                    movieball_link = '#'
                    d.data['moviedex'].append(moviemon_id)
                else:
                    missed = True
            d.save_state()
    if d.capturable == moviemon_id:
        return render(request, "battle.html", {
            'poster': movie['poster'],
            'balls_number': d.data['nbr_movieball'],
            'player_strength': player_strength,
            'success_proba': success_proba,
            'captured': captured,
            'missed': missed,
            'movieball_toss_link': movieball_link,
            'worldmap_link' : 'http://127.0.0.1:8000/worldmap',
            'moviemon_strength': movie['rating']
            })
    else:
        raise Http404()