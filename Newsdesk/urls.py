from django.urls import path

from Newsdesk.views import index


app_name = "newsdesk"


urlpatterns = [
    path("", index, name="index"),
]
