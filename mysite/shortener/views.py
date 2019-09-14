from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView
from .models import Url


class UrlCreateView(CreateView):
    model = Url
    template_name = 'shortener/home.html'
    fields = ['url_original']

    def get_context_data(self, **kwargs):
        context = super(UrlCreateView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["site_list"] = self.model.objects.filter(author=self.request.user).order_by('-date_created')           
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.instance.author)
        return super().form_valid(form)


def link(request, url_short):
    query = Url.objects.get(url_short=url_short)
    query.clicks += 1
    query.save()
    link = query.url_original

    return HttpResponseRedirect(link)
