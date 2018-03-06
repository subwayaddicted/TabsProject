from django.shortcuts import render
from pprint import pprint
from .models import Artist, Album, Song

# Create your views here.
def main_page(request):
    return render(request, 'mainApp/main_page.html', {})

def view_page(request):
    artists = Artist.objects.filter(id__gt=0)
    return render(request, 'mainApp/view_page.html', {'artists':artists})