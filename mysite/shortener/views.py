from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Url

# Create your views here.
def detail(request, url_id):
    url = get_object_or_404(Url, pk=url_id )
    return render(request, 'shortener/detail.html', {'url': url})

def home(request):
    latest_url_list = Url.objects.order_by('-date_created')[:5]
    context = {
        'site_list': latest_url_list,
    }
    return render(request,'shortener/home.html', context)


    #1. Если url есть в базе, значит ссылка была создана и отдать эту ссылку
    #2. Если урл в базе нет, сгенерировать ссылку и дать ее
    #3. Как придумать счетчик переходов