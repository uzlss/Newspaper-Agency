from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from Newsdesk.forms import RedactorCreationForm, RedactorUpdateNewspapersForm
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


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newsdesk:topic-list")

class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newsdesk:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newsdesk:topic-list")
    template_name_suffix = "_confirm_delete"


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 5


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    queryset = Newspaper.objects.all().select_related("topic")
    queryset = queryset.prefetch_related("publishers")


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("newsdesk:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("newsdesk:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newsdesk:newspaper-list")
    template_name_suffix = "_confirm_delete"


class ToggleNewspaperRedactor(LoginRequiredMixin, generic.View):

    def post(self, request, pk, *args, **kwargs):
        newspaper = Newspaper.objects.get(pk=pk)
        redactor = request.user
        if (
            newspaper in redactor.newspapers.all()
        ):
            redactor.newspapers.remove(pk)
        else:
            redactor.newspapers.add(pk)
        return HttpResponseRedirect(
            reverse_lazy("newsdesk:newspaper-detail", kwargs={"pk": pk})
        )


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 10


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newsdesk:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateNewspapersForm
    success_url = reverse_lazy("newsdesk:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newsdesk:redactor-list")
    template_name_suffix = "_confirm_delete"
