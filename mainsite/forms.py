from django import forms


class QueryForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField()
    subject = forms.CharField(max_length=40)
    message = forms.CharField()
