from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import TweetCreationForm
from .models import Tweet, User


def HomeView(request):
    tweets_list = Tweet.objects.all()
    return render(request, "tweets/home.html", {"tweets_list": tweets_list})


def TweetDetailView(request, pk):
    tweets = Tweet.objects.filter(id=pk)
    return render(request, "tweets/detail.html", {"tweets": tweets})


def TweetDeletesView(request, pk):
    tweets = Tweet.objects.filter(id=pk)
    return render(request, "tweets/delete.html", {"tweets": tweets})


def TweetDeleteView(request, pk):
    tweets = Tweet.objects.filter(id=pk)
    if tweets.count() == 0:
        return HttpResponseNotFound()
    if request.user != tweets[0].user:
        return HttpResponseForbidden()
    tweets.delete()
    return redirect("tweets:home")


class TweetCreationView(CreateView):
    template_name = "tweets/post.html"
    form_class = TweetCreationForm
    success_url = "/tweets/home/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
