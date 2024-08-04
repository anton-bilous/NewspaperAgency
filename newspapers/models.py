from django.db import models
from django.contrib.auth.models import AbstractUser


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=4095)
    published_date = models.DateField(auto_now_add=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="newspapers"
    )
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")
