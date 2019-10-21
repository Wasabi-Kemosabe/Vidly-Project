from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre

# Create your views here.


def index(request):
    # Read data from DB
    genres = Genre.objects.all()
    # Send data and render html
    return render(request, 'views/index.html', {'title': 'Index Page', 'items': genres})


def welcome(request):
    return render(request, 'views/welcome.html', {'title': 'Welcome', 'rows': 2})


def about(request):
    return HttpResponse("<h1>About Page</h1><h3>&copy; 2019 Angelo Totanes</h3>")


def catalog(request):
    return render(request, 'views/catalog.html')
