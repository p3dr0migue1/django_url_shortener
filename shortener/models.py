from django.db import models

from .utils import code_generator


class URL(models.Model):
    full_url = models.URLField(max_length=220)
    short_generated_url = models.CharField(
        max_length=15,
        unique=True,
        blank=True
    )
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def create_shortcode(self, size=6):
        new_code = code_generator(size=size)
        short_url_exists = self.__class__.objects.filter(
            short_generated_url=new_code
        ).exists()

        if short_url_exists:
            return self.create_shortcode(size=6)
        return new_code

    def save(self, *args, **kwargs):
        if self.short_generated_url is None or self.short_generated_url == "":
            self.short_generated_url = self.create_shortcode()
        super(URL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.full_url)

    def __unicode__(self):
        return str(self.full_url)
