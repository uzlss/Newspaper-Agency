from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from Newsdesk.models import Newspaper


class RedactorCreationForm(UserCreationForm):
    newspapers = forms.ModelMultipleChoiceField(
        queryset=Newspaper.objects,
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("years_of_experience", "newspapers")


class RedactorUpdateNewspapersForm(forms.ModelForm):
    newspapers = forms.ModelMultipleChoiceField(
        queryset=Newspaper.objects,
        required=False
    )

    class Meta:
        model = Newspaper
        fields = ("newspapers", )