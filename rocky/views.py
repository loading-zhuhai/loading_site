from django.shortcuts import render

# Create your views here.

def rocky(request):
    return render(request, "rocky.html", {})

