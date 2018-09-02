from django.forms import Form, CharField
from .validators import validate_url


class SubmitURLForm(Form):
    url = CharField(label='Submit URL', validators=[validate_url])
