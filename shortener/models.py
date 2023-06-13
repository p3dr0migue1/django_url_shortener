from hashlib import md5

from django.db import models


class URLManager(models.Model):
    def all(self):
        qs = super(URLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs


class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.url_hash)

    def __unicode__(self):
        return str(self.url_hash)
