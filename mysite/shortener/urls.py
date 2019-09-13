from django.urls import path
# from .views import UrlListView, UrlCreateView
from .views import UrlCreateView
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', UrlCreateView.as_view(success_url="/"), name='home'),
    path('<url_short>', views.link, name='link')
]