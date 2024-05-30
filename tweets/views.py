from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView

from .forms import TweetCreationForm
from .models import Tweet


def HomeView(request):
    tweets_list = Tweet.objects.all()
    return render(request, 'tweets/home.html', {'tweets_list': tweets_list})


class TweetCreationView(CreateView):
    template_name = 'tweets/post.html'
    form_class = TweetCreationForm
    success_url = '/tweets/home'
