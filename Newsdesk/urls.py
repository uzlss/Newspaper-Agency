from django.urls import path

from Newsdesk.views import index, TopicListView


app_name = "newsdesk"


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
]
