from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from Newsdesk.models import Newspaper, Topic, Redactor


@login_required
def index(request):
    context = {
        "count_redactors": get_user_model().objects.count(),
        "count_newspapers": Newspaper.objects.count(),
        "count_topics": Topic.objects.count(),
    }
    return render(request, "newsdesk/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 10


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 5


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    queryset = Newspaper.objects.all().select_related("topic")
    queryset = queryset.prefetch_related("publishers")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 10


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
