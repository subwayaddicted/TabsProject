from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'mainApp'

urlpatterns = [
    re_path(r'^$', views.main_page, name = 'main_page'),
    re_path(r'^artists/$', views.view_page, name = 'view_page'),
    re_path(r'^artists/(?P<pk>\d+)/albums/$', views.albums_page, name='albums_page'),
    re_path(r'^artists/(?P<pk>\d+)/albums/songs/$', views.songs_page, name = 'songs_page'),
    re_path(r'^profile/(?P<pk>\d+)/personal_area/$', views.personal_area_page, name = 'personal_area_page'),
    path(r'about/', views.about_page, name='about_page'),
    path(r'contact/', views.contact_page, name = 'contact_page'),
    path(r'new_artist/', views.new_artist_page, name = 'new_artist_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)