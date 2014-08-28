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


class Pin(models.Model):
    created_by = models.ForeignKey(User)
    board = models.ForeignKey(Board)
    image = models.ImageField(upload_to="pins")
    description = models.TextField()

    def __unicode__(self):
        return u"%s - %s" % (self.board, self.description)

