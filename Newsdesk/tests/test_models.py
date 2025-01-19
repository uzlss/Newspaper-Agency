from django.contrib.auth import get_user_model
from django.test import TestCase

from Newsdesk.models import Topic, Newspaper


class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.topic = Topic.objects.create(name="Test Topic")
        cls.redactor = get_user_model().objects.create_user(
            username="test_user",
            password="password",
            first_name="test_first_name",
            last_name="test_last_name",
        )
        cls.newspaper = Newspaper(
            title="Test Newspaper",
            content="Test Newspaper content",
            topic=cls.topic,
        )
        cls.newspaper.save()
        cls.newspaper.publishers.add(cls.redactor)

    def test_topic_str(self):
        self.assertEqual(str(self.topic), self.topic.name)

    def test_redactor_str(self):
        self.assertEqual(
            str(self.redactor),
            f"{self.redactor.username} ({self.redactor.first_name} {self.redactor.last_name})"
        )

    def test_newspaper_str(self):
        self.assertEqual(
            str(self.newspaper),
            f"{self.newspaper.title} ({self.newspaper.topic})"
        )

    def test_redactor_without_experience(self):
        self.assertEqual(
            self.redactor.years_of_experience, 0
        )

    def test_redactor_with_experience(self):
        redactor = self.redactor.copy()
        redactor.years_of_experience = 20
        redactor.save()
        self.assertEqual(redactor.years_of_experience, 20)
