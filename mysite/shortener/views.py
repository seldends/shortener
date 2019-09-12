from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from .models import Url


class UrlCreateView(CreateView):
    model = Url
    template_name = 'shortener/home.html'
    fields = ['url_original']

    def get_context_data(self, **kwargs):
        context = super(UrlCreateView, self).get_context_data(**kwargs)
        context["site_list"] = self.model.objects.order_by('-date_created')
        return context


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
