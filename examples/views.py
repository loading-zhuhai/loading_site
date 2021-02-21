from django.shortcuts import render

# Create your views here.

def examples(request):
    return render(request, "nate_example.html", {})
def examples(request):
    return render(request, "joanne_example.html", {})
