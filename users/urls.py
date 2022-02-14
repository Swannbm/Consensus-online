from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('', views.Connectview.as_view(), name="connect"),
    path('inscription', views.SubscriptionView.as_view(), name="subscription"),
    path('profile', views.Connectview.as_view(), name="profile"),
    path('deconnexion', views.Disconnectview.as_view(), name="disconnect"),
]
