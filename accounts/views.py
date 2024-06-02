from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView

from .forms import LoginForm, SignupForm


class SignupView(CreateView):

    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):

        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"


class LogoutView(BaseLogoutView):
    success_url = settings.LOGOUT_REDIRECT_URL
