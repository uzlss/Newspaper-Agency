from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Newsdesk.models import Topic, Newspaper


class TestViews(TestCase):
    fixtures = ["Newsdesk/fixtures/test_data.json"]

    def setUp(self):
        user = get_user_model().objects.create_user(
            username="Test User",
            password="<PASSWORD>",
        )
        self.client.force_login(user)

    def test_home_page(self):
        url = reverse("newsdesk:index")
        response = self.client.get(url)
        self.assertContains(response, get_user_model().objects.count())
        self.assertContains(response, Topic.objects.count())
        self.assertContains(response, Newspaper.objects.count())

    def test_topic_list_paginated(self):
        pagination_num = 10
        url = reverse("newsdesk:topic-list")
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["topic_list"]),
            pagination_num,
            f"topic-list must be paginated to {pagination_num}"
        )

    def test_newspaper_list_paginated(self):
        pagination_num = 5
        url = reverse("newsdesk:newspaper-list")
        response = self.client.get(url)
        self.assertContains(response, Newspaper.objects.get(pk=1).title)
        self.assertEqual(
            len(response.context["newspaper_list"]),
            pagination_num,
            f"newspaper-list must be paginated to {pagination_num}")

    def test_redactors_list_paginated(self):
        pagination_num = 10
        url = reverse("newsdesk:redactor-list")
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["redactor_list"]),
            pagination_num,
            f"redactor-list must be paginated to {pagination_num}"
        )


class TestLoginView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.newspaper = Newspaper(
            id=1,
            title="Test Newspaper",
            content="Test content",
            topic=Topic.objects.create(name="Test Topic"),
        )
        cls.publisher = get_user_model().objects.create_user(
            username="Test User",
            password="<PASSWORD>",
        )
        cls.newspaper.publishers.add(cls.publisher)
        cls.newspaper.save()

    def test_home_page_login_required(self):
        url = reverse("newsdesk:index")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_topic_list_login_required(self):
        url = reverse("newsdesk:topic-list")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_newspaper_list_login_required(self):
        url = reverse("newsdesk:newspaper-list")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_redactor_list_login_required(self):
        url = reverse("newsdesk:redactor-list")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_newspaper_detail_login_required(self):
        url = reverse("newsdesk:newspaper-detail", args=[self.newspaper.id])
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_redactor_detail_login_required(self):
        url = reverse("newsdesk:redactor-detail", args=[self.publisher.id])
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)
