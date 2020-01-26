from django.shortcuts import render
from common import game
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary[key]

# Create your views here.
def moviedex_f(request):
    d = game.data_game()
    d.load_state()
    return render(request, "moviedex.html", {'movie_list': d.data['list_moviemon'], 'moviedex': d.data['moviedex']})