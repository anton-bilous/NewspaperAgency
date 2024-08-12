from django.test import TestCase
from django.db import IntegrityError

from .models import Topic, Newspaper


class TestTopicModel(TestCase):
    def test_str(self):
        name = "Test"
        topic = Topic.objects.create(name=name)
        self.assertEqual(str(topic), name)

    def test_cant_create_empty_topic(self):
        with self.assertRaises(IntegrityError):
            Topic.objects.create()


class TestNewspaperModel(TestCase):
    def test_str(self):
        title = "Test"
        topic = Topic.objects.create(name="Test topic")
        newspaper = Newspaper.objects.create(
            title=title, content="Abc", topic=topic
        )
        self.assertEqual(str(newspaper), title)
