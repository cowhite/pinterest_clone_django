import os, re
from django import template
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.inclusion_tag("inclusion_tags/is_following.html")
def is_following(user, object):
    content_type_obj = content_type(object)
    return {
                "user": user,
                "content_type": content_type_obj,
                "object": object,
                "is_following": user.is_following(content_type_obj.id, object.id)
           }


@register.filter
def content_type(instance):
    if not instance:
        return False
    return ContentType.objects.get_for_model(instance)

