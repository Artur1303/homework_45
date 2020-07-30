from django import forms
from django.forms import widgets
from .models import STATUS_CHOICES

BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'
default_status = STATUS_CHOICES[0][0]


class TodoForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Title')
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Status')
    descriptions = forms.CharField(max_length=3000, required=True, label='Descriptions', widget=forms.Textarea)
    data = forms.DateField(required=False, label='Время Завершение', widget=forms.DateInput(attrs={'type': 'date'}))