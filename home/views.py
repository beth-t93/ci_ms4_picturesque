from django.shortcuts import render

def index(request):
    return render(request, "home/index.html")
""" A view to return to the index page """
