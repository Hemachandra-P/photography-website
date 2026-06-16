from django.shortcuts import render
from .models import Photo

def home(request):
    portraits = Photo.objects.filter(category='portrait')
    landscapes = Photo.objects.filter(category='landscape')

    return render(request, 'home.html', {
        'portraits': portraits,
        'landscapes': landscapes
    })