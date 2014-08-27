from django.contrib.auth.models import User
from django.db import models

from util.models import Slugged

class Board(Slugged):
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('BoardCategory', null=True, blank=True)
    user = models.ForeignKey(User)

    class Meta:
        abstract = False

    def __unicode__(self):
        return u"%s" % self.name


class BoardCategory(Slugged):
    class Meta:
        abstract = False

