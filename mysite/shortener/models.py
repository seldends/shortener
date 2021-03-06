import string
import requests
from random import choices

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.


class Url(models.Model):
    url_original = models.CharField(max_length=200)
    url_short = models.CharField(default=None, max_length=6, unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    clicks = models.IntegerField(default=0)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.url_original

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.url_short is None:
            self.url_short = self.generate_short_link()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        url_short = ''.join(choices(characters, k=6))
        if Url.objects.filter(url_short=url_short).first():
            return self.generate_short_link()
        return url_short

    def get_short_url(self):
        url_path = reverse('shortener:link', kwargs={'url_short': self.url_short})
        return url_path

    def clean(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:65.0) Gecko/20100101 Firefox/65.0'
        }
        try:
            requests.get(self.url_original, headers=headers)
        except(requests.RequestException, ValueError):
            raise ValidationError({'url_original': 'Введите корректный URL'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
