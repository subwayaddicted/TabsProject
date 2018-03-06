from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path(r'', views.main_page, name = 'main_page'),
    path(r'artists/', views.view_page, name = 'view_page'),
    path(r'artists/albums/', views.albums_page, name='albums_page'),
    path(r'artists/albums/songs/', views.songs_page, name = 'songs_page'),
    path(r'about/', views.about_page, name='about_page'),
    path(r'contact/', views.contact_page, name = 'contact_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)