from django.urls import path

from Newsdesk.views import (
    index,
    TopicListView,
    NewspaperListView,
    NewspaperDetailView,
    RedactorListView,
    RedactorDetailView,
    TopicCreateView,
    TopicUpdateView,
    NewspaperCreateView,
    NewspaperUpdateView,
    RedactorCreateView,
    RedactorUpdateView,
    TopicDeleteView,
    NewspaperDeleteView,
    RedactorDeleteView,
    ToggleNewspaperRedactor,
)


app_name = "newsdesk"


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(), name="topic-update"
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path(
        "news/",
        NewspaperListView.as_view(),
        name="newspaper-list"
    ),
    path(
        "news/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "news/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "news/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "news/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
    path(
        "news/<int:pk>/toggle_assign/",
        ToggleNewspaperRedactor.as_view(),
        name="newspaper-toggle-assign",
    ),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update",
    ),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
]
