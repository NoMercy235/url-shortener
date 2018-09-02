from django.db import models

"""
Run the following two commands if you ever change something in this models file.

python manage.py makemigrations
python manage.py migrate


If you forgot, and stuff starts to break, delete the sqlite databse and run the command below along with the two above

python manage.py createsuperuser
"""

class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=20, null=False, blank=False, default='testval', unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
