from django.contrib.auth.models import User
from django.db import models

from util.models import Slugged

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('BoardCategory', null=True, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u"%s" % self.name


class BoardCategory(Slugged):
    class Meta:
        abstract = False

