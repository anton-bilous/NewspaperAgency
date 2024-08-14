from datetime import date, timedelta

from django.views import generic
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Redactor, Topic, Newspaper, VisitCounter
from .forms import NewspaperForm, RedactorSearchForm, NewspaperSearchForm


def index(request):
    visit_counter = VisitCounter.load()
    visit_counter.total_count += 1
    visit_counter.logged_in_count += request.user.is_authenticated
    visit_counter.save()

    now = date.today()
    dates = []
    counts = []
    for day in range(6, -1, -1):
        day_to_check = now - timedelta(days=day)
        dates.append(day_to_check.strftime("%Y-%m-%d"))
        counts.append(
            Newspaper.objects.filter(published_date=day_to_check).count()
        )

    context = {
        "num_redactors": Redactor.objects.count(),
        "num_topics": Topic.objects.count(),
        "num_newspapers": Newspaper.objects.count(),
        "dates": dates,
        "newspaper_counts": counts,
        "total_visit_count": visit_counter.total_count,
        "logged_in_visit_count": visit_counter.logged_in_count,
        "anonymous_visit_count": visit_counter.total_count
        - visit_counter.logged_in_count,
    }
    return render(request, "newspapers/index.html", context=context)


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        form = RedactorSearchForm(self.request.GET)

        queryset = Redactor.objects.all()
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = ("name",)
    success_url = reverse_lazy("newspapers:topics")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        form = NewspaperSearchForm(self.request.GET)

        queryset = Newspaper.objects.select_related("topic")
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspapers:newspapers")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        return reverse(
            "newspapers:newspaper-detail", args=(self.get_object().id,)
        )
