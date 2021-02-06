from django.shortcuts import render

# Create your views here.

def joanne(request):
    return render(request, 'joanne.html', {})
