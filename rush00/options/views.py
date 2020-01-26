from django.shortcuts import render

# Create your views here.
def options_f(request):
    return render(request, "options.html", {"save_link":'save_game', "titlescreen_link":'http://127.0.0.1:8000/', "worldmap_link":"http://127.0.0.1:8000/worldmap"})