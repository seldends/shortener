from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.views import View
from .models import Url
#from .forms import UrlForm


class UrlListView(ListView):
    model =  Url
    template_name = 'shortener/home.html'
    context_object_name = 'site_list'
    ordering = ['-date_created']


class UrlCreateView(CreateView):
    model =  Url
    template_name = 'shortener/home.html'
    fields = ['url_original']
    #context_object_name = 'site_list'

    def get_context_data(self, **kwargs):
        context = super(UrlCreateView, self).get_context_data(**kwargs)
        context["site_list"] = self.model.objects.order_by('-date_created')
        return context
        
   
    #1. Если url есть в базе, значит ссылка была создана и отдать эту ссылку
    #2. Если урл в базе нет, сгенерировать ссылку и дать ее
    #3. Как придумать счетчик переходов