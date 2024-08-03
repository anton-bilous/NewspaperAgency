from django.db import models
from django.contrib.auth.models import AbstractUser


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)
