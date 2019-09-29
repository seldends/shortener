from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from .models import Url
from .forms import UrlForm
from django.views import View


class UrlCreateView(CreateView):
    model = Url
    template_name = 'shortener/home.html'
    form_class = UrlForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UrlCreateView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["site_list"] = self.model.objects.filter(author=self.request.user).order_by('-date_created')
        return context


class UrlRedirectView(View):
    @classmethod
    def get(self, request, *args, **kwargs):
        url_short = kwargs['url_short']
        try:
            with transaction.atomic():
                query = Url.objects.select_for_update().get(url_short=url_short)
                query.clicks += 1
                query.save()
                url = query.url_original
                return HttpResponseRedirect(url)
        except ObjectDoesNotExist:
            template_name = "shortener/404.html"
            return render(request, template_name)
