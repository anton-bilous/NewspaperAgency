from django.urls import path

from .views import index, RedactorListView


app_name = "newspapers"

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactors"),
]
