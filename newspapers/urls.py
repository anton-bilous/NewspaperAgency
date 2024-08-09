from django.urls import path

from .views import (
    index,
    RedactorListView,
    RedactorDetailView,
    TopicListView,
    TopicCreateView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
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
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail",
    ),
    path(
        "newspapers/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create",
    ),
]
