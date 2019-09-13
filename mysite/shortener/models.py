import string
from random import choices

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
import requests
from django.core.exceptions import ValidationError

# Create your models here.


class Url(models.Model):
    url_original = models.CharField(max_length=200, unique=True, error_messages={'unique': 'URL уже есть в базе'})
    url_short = models.CharField(default=None, max_length=20, unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    clicks = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.url_original

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.url_short is None:
            self.url_short = self.generate_short_link()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        url_short = ''.join(choices(characters, k=6))
        # if Url.object.filer_by(url_short=url_short).first():
        #     return self.generate_short_link()
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

        if self.author is None:
            raise ValidationError({'url_original': 'Вам необходимо войти'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
