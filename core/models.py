from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from util.models import Slugged
from util.utils import content_type_object

class Board(Slugged):
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('BoardCategory', null=True, blank=True)
    user = models.ForeignKey(User)

    class Meta:
        abstract = False

    def __unicode__(self):
        return u"%s" % self.name

    def get_content_type(self):
        return ContentType.objects.get(app_label="core", name="board")


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


class Follow(models.Model):
    followed_by = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


#model methods for User

def follow(self, content_type_id, object_id):
    content_type_object(content_type_id, object_id)

    obj, created = Follow.objects.get_or_create(followed_by=self, content_type_id=content_type_id, object_id=object_id)
    return created

def unfollow(self, content_type_id, object_id):
    content_type_object(content_type_id, object_id)
    try:
        obj = Follow.objects.get(followed_by=self, content_type_id=content_type_id, object_id=object_id)
        obj.delete()
        if obj.id:
            return False
        return True
    except Follow.DoesNotExist:
        return False

def is_following(self, content_type_id, object_id):
    content_type_object(content_type_id, object_id)
    try:
        obj = Follow.objects.get(followed_by=self, content_type_id=content_type_id, object_id=object_id)
        return True
    except Follow.DoesNotExist:
        return False

def get_content_type(self):
    return ContentType.objects.get(app_label="core", name="board")


User.add_to_class("follow", follow)
User.add_to_class("unfollow", unfollow)
User.add_to_class("is_following", is_following)
