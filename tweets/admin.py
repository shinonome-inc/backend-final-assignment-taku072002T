# from django.contrib import adm        in
from django.contrib import admin

from .models import Tweet

admin.site.register(Tweet)
