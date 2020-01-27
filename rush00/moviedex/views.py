from django.shortcuts import render
from common import game
from django.template.defaulttags import register
from django.conf import settings
from common import game

@register.filter
def get_item(dictionary, key):
    return dictionary[key]

# Create your views here.
def moviedex_f(request):
    d = game.data_game()
    d.load_state()

    selector = game.Selector()
    if request.method == "POST":
        if 'left' in request.POST and selector.slot_place > 0:
            selector.minus()
        elif 'right' in request.POST and selector.slot_place < len(d.data['moviedex']) - 1:
            selector.plus()

    return render(request, "moviedex.html",{
        'movie_list': d.data['list_moviemon'],
        'moviedex': d.data['moviedex'],
        'arrow_pos': selector.slot_place,
        'detail_link': 'http://127.0.0.1:8000/moviedex/' + d.data['moviedex'][selector.slot_place] + '/'})
