import string
from random import choices

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Url(models.Model):
    url_original = models.CharField(max_length=200, unique=True, error_messages={'unique': 'URL уже есть в базе'})
    url_short = models.CharField(default=None, max_length=20, unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.url_original
    

    def __init__(self, *args, **kwargs):
        # if self.query.filer_by(url_original=url_original).first()==None:
        super().__init__(*args, **kwargs)
        if self.url_short == None:
            self.url_short = self.generate_short_link()

            
    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        url_short = ''.join(choices(characters, k=6))
        # if Url.object.filer_by(url_short=url_short).first():
        #     return self.generate_short_link()
        return url_short

    def get_short_url(self):
        # url_path = reverse("shortcode", shortcode=self.url_short)
        return "http://127.0.0.1:8000/{shortcode}".format(shortcode=self.url_short)
