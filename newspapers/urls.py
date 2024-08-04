from django.urls import path

from .views import (
    index,
    RedactorListView,
    RedactorDetailView,
    TopicListView,
    TopicCreateView,
    NewspaperListView,
)


app_name = "newspapers"

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactors"),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail",
    ),
    path("topics/", TopicListView.as_view(), name="topics"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("newspapers/", NewspaperListView.as_view(), name="newspapers"),
]
