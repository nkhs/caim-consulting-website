from django import forms
from mainsite.models import Service


class QueryForm(forms.Form):
    subject = forms.CharField(max_length=40)
    message = forms.CharField()
    service = forms.ModelChoiceField(queryset=Service.objects.all())
