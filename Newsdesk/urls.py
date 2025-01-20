from django.urls import path

from Newsdesk.views import (
    index,
    TopicListView,
    NewspaperListView,
    NewspaperDetailView,
)


app_name = "newsdesk"


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("news/", NewspaperListView.as_view(), name="newspaper-list"),
    path("news/<int:pk>", NewspaperDetailView.as_view(), name="newspaper-detail"),
]
