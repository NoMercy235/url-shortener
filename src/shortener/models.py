from django.db import models
from .utils import create_shortcode

"""
Run the following two commands if you ever change something in this models file.

python manage.py makemigrations
python manage.py migrate


If you forgot, and stuff starts to break, delete the sqlite databse and run the command below along with the two above

python manage.py createsuperuser
"""


class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super().all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = KirrURL.objects.filter(id__gte=1)
        new_codes = 0
        for obj in qs:
            obj.shortcode = create_shortcode(obj)
            obj.save()
            new_codes +=1
        return 'New codes made: {i}'.format(i=new_codes)


class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=20, null=False, blank=False, default='testval', unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    # Overriding the object property of the KirrURL class. It can have different name if you don't want to override.
    objects = KirrURLManager()

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '' or self.shortcode == '__placeholder__':
            self.shortcode = create_shortcode()
        super().save(*args, **kwargs)
