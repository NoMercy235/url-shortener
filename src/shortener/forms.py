from django.forms import Form, CharField
from .validators import validate_url


class SubmitURLForm(Form):
    url = CharField(label='Submit URL', validators=[validate_url])

    def clean_url(self):
        value = self.cleaned_data.get('url')
        if not value.startswith('http'):
            value = 'http://' + value
        return value

