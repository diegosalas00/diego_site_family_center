from django import forms
from django.core import validators

from activities.models import snacks, drinks, activities


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class ReservedForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email address")
    date = forms.DateTimeField(label="Enter your reservation date")
    activity = forms.CharField(
        max_length=25,
        widget=forms.Select(choices=activities),
        label="Activities",
    )
    party_packages = forms.CharField()
    drink = forms.CharField(
        max_length=25,
        widget=forms.Select(choices=drinks),
        label="Drinks",
    )
    snack = forms.CharField(
        max_length=25,
        widget=forms.Select(choices=snacks),
        label="Snacks",
    )
    questions = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label="Do you have any questions for us?",
    )
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave empty",
                               validators=[validators.MaxLengthValidator(0)]
                               )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields"
            )
