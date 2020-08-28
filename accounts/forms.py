from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    username.widget.attrs.update({"class": "form-control"})
    email.widget.attrs.update({"class": "form-control"})
    first_name.widget.attrs.update({"class": "form-control"})
    last_name.widget.attrs.update({"class": "form-control"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
