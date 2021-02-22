from django.shortcuts import render

# Create your views here.


def joanne_examples(request):
    return render(request, "joanne_examples.html", {})
