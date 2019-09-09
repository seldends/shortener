from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Url(models.Model):
    url_original = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    url_short = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.url_original

