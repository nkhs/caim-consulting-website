from django import forms


class QueryForm(forms.Form):
    subject = forms.CharField(max_length=40)
    message = forms.CharField()
