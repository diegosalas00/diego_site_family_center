from django import forms

from . import models


class ActivityForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = [
            'title',
            'description',
            'order',
        ]


class PartyPackageForm(forms.ModelForm):
    class Meta:
        model = models.PartyPackage
        fields = [
            'title',
            'description',
            'content',
            'order',
            'activity',
        ]


class AvailableForm(forms.ModelForm):
    class Meta:
        model = models.Available
        fields = [
            'name',
            'activity',
            'package',
            'date_start',
            'date_end',
            'description',
            'snack',
            'drink',
            'order',
        ]


