from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path(r'', views.main_page, name = 'main_page'),
    path(r'tabs/', views.view_page, name = 'view_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)