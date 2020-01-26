from django.shortcuts import render

# Create your views here.
def load_f(request):
    return render(request, "load.html")