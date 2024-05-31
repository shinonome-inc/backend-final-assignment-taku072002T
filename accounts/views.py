from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from tweets.models import Tweet

from .forms import LoginForm, SignupForm
from .models import Connection, User


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("tweets:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response


def UserProfileView(request, username):
    tweets_list = Tweet.objects.filter(user=User.objects.get(username=username))
    return render(request, "tweets/profile.html", {"username": username, "tweets_list": tweets_list})



def follow_view(request, user):
    try:
        follower = User.objects.get(username=request.user.username)
        following = User.objects.get(username=user)

    except User.DoesNotExist:
        messages.warning(request, "User does not exist")
    if follower == following:
        messages.warning(request, 'You cannot follow your self.')
    else:
        created = Connection.objects.create(follower=follower, following=following)
        if (created):
            messages.success(request, '{}をフォローしました。'.format(following.username))
        else:
            messages.success(request, f'You are now following {following.username}')
    return redirect('tweets:home')


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"


class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("/")
