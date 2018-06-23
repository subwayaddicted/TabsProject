from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'sign_up/', views.sign_up_view , name = 'sign_up_page'),
    re_path(r'log_in/', views.log_in_view , name = 'log_in_page'),
    re_path(r'log_out/', views.log_out_view , name = 'log_out_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)