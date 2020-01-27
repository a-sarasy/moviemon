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
    if len(d.data['moviedex']):

        if request.method == "POST":
            if 'left' in request.POST:
                selector.minus(d.data)
            elif 'right' in request.POST:
                selector.plus(d.data)
        else:
            selector.reset(d.data)
        detail_link = 'http://127.0.0.1:8000/moviedex/' + selector.slot_place + '/'
    else:
        selector.slot_place = ""
        detail_link = '#'
    print(selector.slot_place)
    return render(request, "moviedex.html",{
        'movie_list': d.data['list_moviemon'],
        'moviedex': d.data['moviedex'],
        'selector_pos': selector.slot_place,
        'detail_link': detail_link,
        'len_moviedex': len(d.data['moviedex']),
        'worldmap_link': 'http://127.0.0.1:8000/worldmap/' })
