from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from util.models import Slugged
from util.utils import content_type_object, get_content_type

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
    content_type, content_object = content_type_object(content_type_id, object_id)

    obj, created = Follow.objects.get_or_create(followed_by=self, content_type_id=content_type_id, object_id=object_id)

    #If a user follows a user, follow all his boards
    if content_type.model_class() is User:
        for board in content_object.board_set.all():
            self.follow(get_content_type(board).id, board.id)
    return created, content_type, content_object

def unfollow(self, content_type_id, object_id):
    content_type, content_object = content_type_object(content_type_id, object_id)

    #If a user unfollows a user, unfollow all his boards
    if content_type.model_class() is User:
        for board in content_object.board_set.all():
            self.unfollow(get_content_type(board).id, board.id)
    try:
        obj = Follow.objects.get(followed_by=self, content_type_id=content_type_id, object_id=object_id)
        obj.delete()
        if obj.id:
            return False, content_type, content_object
        return True, content_type, content_object
    except Follow.DoesNotExist:
        return False, content_type, content_object



def is_following(self, content_type_id, object_id):
    content_type_object(content_type_id, object_id)
    try:
        obj = Follow.objects.get(followed_by=self, content_type_id=content_type_id, object_id=object_id)
        return True
    except Follow.DoesNotExist:
        return False


User.add_to_class("follow", follow)
User.add_to_class("unfollow", unfollow)
User.add_to_class("is_following", is_following)
