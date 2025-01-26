from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from Newsdesk.models import Newspaper


class RedactorCreationForm(UserCreationForm):
    newspapers = forms.ModelMultipleChoiceField(
        queryset=Newspaper.objects, required=False
    )

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "email",
            "years_of_experience",
            "newspapers",
        )


class RedactorUpdateNewspapersForm(forms.ModelForm):
    newspapers = forms.ModelMultipleChoiceField(
        queryset=Newspaper.objects, required=False
    )

    class Meta:
        model = get_user_model()
        fields = ("newspapers",)


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": ("form-control form-control-lg"
                          " border-1 text-white white-placeholder"),
                "placeholder": "Search...",
                "style": "background: transparent;",
            }
        ),
    )
