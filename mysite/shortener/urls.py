from django.urls import path
from .views import UrlListView, UrlCreateView
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', UrlCreateView.as_view(success_url="/"), name='home'),
    #path('<int:url_id>/', views.detail, name='detail'),
]