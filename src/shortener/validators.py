from django import forms
from django.core.validators import URLValidator


def validate_url(value: str):
    if not value.startswith('http://') or not value.startswith('https://'):
        value = 'https://' + value

    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise forms.ValidationError('Invalid URL for this field')
    return value
