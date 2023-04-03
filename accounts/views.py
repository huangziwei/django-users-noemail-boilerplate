from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView

from .forms import CustomUserCreationForm

User = get_user_model()


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class HomePageView(TemplateView):
    template_name = "home.html"


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "account_detail.html"


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User

    fields = [
        "username",
        "name",
        "bio",
    ]

    template_name = "account_update.html"

    def get_success_url(self):
        return reverse("home")

    def get_object(self):
        return User.objects.get(username=self.request.user.username)
