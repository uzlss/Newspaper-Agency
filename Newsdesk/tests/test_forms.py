from django.test import TestCase

from Newsdesk.forms import RedactorCreationForm
from Newsdesk.models import Newspaper, Topic


class TestRedactorCreationForm(TestCase):

    def setUp(self):
        self.form_data = {
            "username": "test.user",
            "password1": "<PASSWORD>!",
            "password2": "<PASSWORD>!",
            "first_name": "First",
            "last_name": "Last",
            "years_of_experience": 5,
        }

    def test_redactor_creation_form_without_newspapers(self):
        form = RedactorCreationForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_redactor_creation_form_with_newspapers(self):
        topic = Topic.objects.create(
            name="Test Topic",
        )
        newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="Test Content",
            topic=topic,
        )
        form_data = self.form_data.copy()
        form_data["newspapers"] = [newspaper]
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
