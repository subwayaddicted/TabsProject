from django.shortcuts import render, get_object_or_404
from pprint import pprint
from .models import Artist, Album, Song

# Create your views here.


def main_page(request):
    return render(request, 'mainApp/main_page.html', {})


def view_page(request):
    artists = Artist.objects.filter(id__gt=0)
    return render(request, 'mainApp/view_page2.html', {'artists':artists})


def albums_page(request, pk):
    albums = Album.objects.filter(artist_id=pk)
    return render(request, 'mainApp/albums_page.html', {'albums': albums})


def songs_page(request, pk):
    songs = Song.objects.filter(album_id=pk)
    return render(request, 'mainApp/songs_page.html', {'songs': songs})


def about_page(request):
    return render(request, 'mainApp/about_page.html', {})


def contact_page(request):
    return render(request, 'mainApp/contact_page.html', {})