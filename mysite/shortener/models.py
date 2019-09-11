from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import string
from random import choices
# Create your models here.

class Url(models.Model):
    url_original = models.CharField(max_length=200, unique=True)
    url_short = models.CharField(default=None, max_length=20, unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.url_original
    
    # def get_absolute_url(self):
    #     return reverse('')
    def __init__(self, *args, **kwargs):
        # try:
        super().__init__(*args, **kwargs)
        #print(self.url_short )
        if self.url_short == None:
            self.url_short = self.generate_short_link()
        #print(self.url_short)
        # except:
        #     print(self.url_short )
            
    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        url_short = ''.join(choices(characters, k=6))
        # link = self.query.filer_by(url_short=url_short).first()
        # if link:
        #     return self.generate_short_link()
        return url_short



