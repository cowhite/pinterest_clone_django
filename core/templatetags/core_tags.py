import os, re
from django import template
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from util.utils import get_content_type

register = template.Library()

@register.inclusion_tag("inclusion_tags/is_following.html")
def is_following(user, object, col):
    content_type_obj = get_content_type(object)
    return {
                "user": user,
                "content_type": content_type_obj,
                "object": object,
                "is_following": user.is_following(content_type_obj.id, object.id),
                "col": col
           }


@register.filter
def content_type(instance):
    return get_content_type(instance)

