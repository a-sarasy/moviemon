from django.shortcuts import render

# Create your views here.
def options_f(request):
    return render(request, "options.html")