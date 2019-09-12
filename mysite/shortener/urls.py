from django.urls import path
from .views import UrlListView, UrlCreateView
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', UrlCreateView.as_view(success_url="/"), name='home'),
    # path('/<url_short>/', UrlDetailView.as_view(), name='url'),
    # path('home/', views.home, name='home2'),
    path('link/<url_short>', views.detail, name='url_detail'),
    path('<url_short>', views.link, name='link'),
    #path('<shortcode>/', views.detail, name='short'),
]