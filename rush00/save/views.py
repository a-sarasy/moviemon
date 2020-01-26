from django.shortcuts import render

# Create your views here.
def save_f(request):
    return render(request, "save.html")