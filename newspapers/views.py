from django.shortcuts import render

from .models import Redactor, Topic, Newspaper


def index(request):
    context = {
        "num_redactors": Redactor.objects.count(),
        "num_topics": Topic.objects.count(),
        "num_newspapers": Newspaper.objects.count(),
    }
    return render(request, "newspapers/index.html", context=context)
