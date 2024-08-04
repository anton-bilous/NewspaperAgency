from django.urls import path

from .views import index


app_name = "newspapers"

urlpatterns = [
    path("", index, name="index"),
]