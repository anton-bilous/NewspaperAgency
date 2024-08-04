from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Redactor, Topic, Newspaper


def index(request):
    context = {
        "num_redactors": Redactor.objects.count(),
        "num_topics": Topic.objects.count(),
        "num_newspapers": Newspaper.objects.count(),
    }
    return render(request, "newspapers/index.html", context=context)


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 10


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
