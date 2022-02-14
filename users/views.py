from django.views.generic import TemplateView, DetailView, CreateView

from .models import User


class Connectview(TemplateView):
    template_name = "users/connect.html"


class Disconnectview(TemplateView):
    template_name = "users/connect.html"


class ProfilView(DetailView):
    model = User
    context_object_name = "user"
    template_name = "users/profile.html"


class SubscriptionView(CreateView):
    model = User
    context_object_name = "user"
    fields = ["email", "first_name"]
    template_name = "users/subscription.html"
