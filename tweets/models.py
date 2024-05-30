import uuid

from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
