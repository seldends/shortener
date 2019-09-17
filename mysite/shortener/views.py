from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.core.exceptions import ObjectDoesNotExist
from .models import Url


class UrlCreateView(CreateView):
    model = Url
    template_name = 'shortener/home.html'
    fields = ['url_original']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UrlCreateView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["site_list"] = self.model.objects.filter(author=self.request.user).order_by('-date_created')           
        return context


def link(request, url_short):
    try:
        query = Url.objects.get(url_short=url_short)
        query.clicks += 1
        query.save()
        link = query.url_original
        return HttpResponseRedirect(link)
    except ObjectDoesNotExist:
        template_name = "shortener/404.html"
        return render(request, template_name)
