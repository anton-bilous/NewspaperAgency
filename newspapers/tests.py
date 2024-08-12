from bs4 import BeautifulSoup
from django.urls import reverse
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model

from .models import Topic, Newspaper


DEFAULT_USER_DATA = {
    "username": "testorius",
    "password": "c3VzYW1vZ3Vz",
}


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

    def test_cant_create_newspaper_with_empty_title(self):
        topic = Topic.objects.create(name="Test topic")
        with self.assertRaises(IntegrityError):
            Newspaper.objects.create(title="", content="Abc", topic=topic)

    def test_cant_create_newspaper_with_empty_content(self):
        topic = Topic.objects.create(name="Test topic")
        with self.assertRaises(IntegrityError):
            Newspaper.objects.create(title="Test", content="", topic=topic)


class PublicTestIndexView(TestCase):
    def test_anonymous_visit_counter(self):
        url = reverse("newspapers:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        bs = BeautifulSoup(response.content, "html.parser")
        self.assertEqual(bs.find(id="anonymous_visit_count").text, "1")

        response = self.client.get(url)
        bs = BeautifulSoup(response.content, "html.parser")
        self.assertEqual(bs.find(id="anonymous_visit_count").text, "2")

    def test_correct_newspapers_count(self):
        url = reverse("newspapers:index")
        topic = Topic.objects.create(name="Test topic")
        Newspaper.objects.create(title="Test", topic=topic, content="Abc")

        response = self.client.get(url)
        self.assertEqual(
            response.context["newspaper_counts"], [0, 0, 0, 0, 0, 0, 1]
        )


class PrivateTestIndexView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(**DEFAULT_USER_DATA)
        self.client.force_login(self.user)

    def test_logged_in_visit_counter(self):
        url = reverse("newspapers:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        bs = BeautifulSoup(response.content, "html.parser")
        self.assertEqual(bs.find(id="logged_in_visit_count").text, "1")

        response = self.client.get(url)
        bs = BeautifulSoup(response.content, "html.parser")
        self.assertEqual(bs.find(id="logged_in_visit_count").text, "2")


class PublicTestRedactorListView(TestCase):
    def test_login_required(self):
        url = reverse("newspapers:redactors")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class PrivateTestRedactorListView(TestCase):
    def setUp(self):
        self.username1 = DEFAULT_USER_DATA["username"]
        self.username2 = "debugius"
        self.user1 = get_user_model().objects.create_user(**DEFAULT_USER_DATA)
        self.user2 = get_user_model().objects.create_user(
            {
                "username": self.username2,
                "password": "YnVncyBhcmUgYW1vbmcgdXMh",
            }
        )
        self.client.force_login(self.user1)

    def test_search(self):
        url = reverse("newspapers:redactors")
        response = self.client.get(url, {"username": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.username1)
        self.assertNotContains(response, self.username2)


class PublicTestRedactorDetailView(TestCase):
    def test_login_required(self):
        url = reverse("newspapers:redactor-detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class PublicTestTopicListView(TestCase):
    def test_login_required(self):
        url = reverse("newspapers:topics")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class PublicTestTopicCreateView(TestCase):
    def test_login_required(self):
        url = reverse("newspapers:topic-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
