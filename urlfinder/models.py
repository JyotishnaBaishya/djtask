from django.db import models
from jsonfield import JSONField

class UrlModel(models.Model):
    url = models.URLField(default='', primary_key=True)
    json = JSONField()

def __str__(self):
    return self.name