from django.shortcuts import render

# Create your views here.

def nathaniel(request):
    return render(request, "nathaniel.html", {})
