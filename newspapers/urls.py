from django.urls import path

from .views import index, RedactorListView, RedactorDetailView


app_name = "newspapers"

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactors"),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail",
    ),
]
