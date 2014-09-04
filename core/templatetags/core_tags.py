import os, re
from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag("inclusion_tags/is_following.html")
def is_following(user, content_type_id, object_id):
    return {
                "user": user,
                "content_type_id": content_type_id,
                "object_id": object_id,
                "is_following": user.is_following(content_type_id, object_id)
           }
