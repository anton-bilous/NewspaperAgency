from django.db import models
from django.contrib.auth.models import AbstractUser


# https://gist.github.com/senko/5028413
class SingletonModel(models.Model):
    """Singleton Django Model
    Ensures there's always only one entry in the database, and can fix the
    table (by deleting extra entries) even if added via another mechanism.
    Also has a static load() method which always returns the object - from
    the database if possible, or a new empty (default) instance if the
    database is still empty. If your instance has sane defaults (recommended),
    you can use it immediately without worrying if it was saved to the
    database or not.
    Useful for things like system-wide user-editable settings.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Save object to the database. Removes all other entries if there
        are any.
        """
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        """
        Load object from the database. Failing that, create a new empty
        (default) instance of the object and return it (without saving it
        to the database).
        """

        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


def check_non_empty(field_name: str) -> models.CheckConstraint:
    return models.CheckConstraint(
        check=~models.Q(field_name, ""), name=f"non_empty_{field_name}"
    )


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        constraints = [check_non_empty("name")]

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

    class Meta:
        constraints = [check_non_empty("title"), check_non_empty("content")]

    def __str__(self) -> str:
        return self.title


class VisitCounter(SingletonModel):
    total_count = models.IntegerField(default=0)
    logged_in_count = models.IntegerField(default=0)
