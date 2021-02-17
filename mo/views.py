from django.shortcuts import render

# Create your views here.

def mo(request):
    return render(request, "mo.html", {})
