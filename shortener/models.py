from django.db import models


class URL(models.Model):
    full_url = models.URLField(max_length=220)
    short_generated_url = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
