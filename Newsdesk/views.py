from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic

from Newsdesk.models import Newspaper, Topic


def index(request):
    context = {
        "count_redactors": get_user_model().objects.count(),
        "count_newspapers": Newspaper.objects.count(),
        "count_topics": Topic.objects.count(),
    }
    return render(request, "newsdesk/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 10


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 5


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
    queryset = Newspaper.objects.all().select_related("topic")
    queryset = queryset.prefetch_related("publishers")
