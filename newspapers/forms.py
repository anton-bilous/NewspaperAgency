from django import forms
from django.contrib.auth import get_user_model

from .models import Newspaper


class NewspaperForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 10}))
    publishers = forms.ModelMultipleChoiceField(
        get_user_model().objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Newspaper
        exclude = ()


class RedactorSearchForm(forms.Form):
    username = forms.CharField(max_length=255, required=False, label="")
