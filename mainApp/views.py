from django.shortcuts import render
from .models import Artist, Album, Song

# Create your views here.
def main_page(request):
    return render(request, 'mainApp/main_page.html', {})

def view_page(request):
    artist = Artist.get(pk=1).order_by('artist_name')
    return render(request, 'mainApp/view_page.html', {})