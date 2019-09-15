from django.urls import path, re_path
from .views import UrlCreateView
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', UrlCreateView.as_view(success_url="/"), name='home'),
    re_path(r'^(?P<url_short>[A-Za-z0-9]{6})$', views.link, name='link')
]