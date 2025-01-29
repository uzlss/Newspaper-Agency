from django.contrib.auth.views import LogoutView
from django.urls import path

from Newsdesk.authentication.views import login_view


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
