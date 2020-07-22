from mainsite.models import Query
from django.forms import ModelForm


class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]
