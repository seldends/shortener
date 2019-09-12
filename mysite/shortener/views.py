from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import Url
#from .forms import UrlForm


# class UrlListView(ListView):
#     model =  Url
#     template_name = 'shortener/url.html'
#     context_object_name = 'site_list'
#     ordering = ['-date_created']


class UrlCreateView(CreateView):
    model =  Url
    template_name = 'shortener/home.html'
    fields = ['url_original']
    #context_object_name = 'site_list'

    def get_context_data(self, **kwargs):
        context = super(UrlCreateView, self).get_context_data(**kwargs)
        #if
        context["site_list"] = self.model.objects.order_by('-date_created')
        return context
        


# def home(request):
#     context = {
#         'site_list': Url.objects.order_by('-date_created')
#     }
#     return render(request, 'shortener/home.html', context)

def detail(request, url_short):
    query = Url.objects.filter(url_short=url_short).first()

    context = {
        'site': query
    }
    return render(request, 'shortener/url.html', context)

def link(request, url_short):
    query = Url.objects.filter(url_short=url_short).first()
    query.clicks = query.clicks + 1
    query.save()
    link = query.url_original
    return HttpResponseRedirect(link)
   
