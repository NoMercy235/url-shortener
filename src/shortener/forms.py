from django.forms import Form, CharField, TextInput
from .validators import validate_url


class SubmitURLForm(Form):
    url = CharField(
        label='',
        validators=[validate_url],
        widget=TextInput(
            attrs={'placeholder': 'URL', 'class': 'form-control'}
        )
    )

    def clean_url(self):
        value = self.cleaned_data.get('url')
        if not value.startswith('http'):
            value = 'http://' + value
        return value

