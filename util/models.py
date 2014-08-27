from django.db import models
from django.template.defaultfilters import slugify

from .utils import base_concrete_model, unique_slug

class Slugged(models.Model):
    #Copied from mezzanine
    name = models.CharField(max_length=500)
    slug = models.CharField(
        max_length=600, null=True, blank=True, unique=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u"%s" % self.name

    def save(self):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Slugged, self).save()

    def generate_unique_slug(self):
        concrete_model = base_concrete_model(Slugged, self)
        slug_qs = concrete_model.objects.exclude(id=self.id)
        return unique_slug(slug_qs, "slug", self.get_slug())

    def get_slug(self):
        return slugify(self.name)
