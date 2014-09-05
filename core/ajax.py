from django.utils import simplejson

from dajaxice.decorators import dajaxice_register

@dajaxice_register
def follow(request, content_type_id, object_id):
    followed = request.user.follow(content_type_id, object_id)
    res = {}
    if followed:
        res['increment'] = 1
    else:
        res['increment'] = 0
    res['content_type_id'] = content_type_id
    res['object_id'] = object_id
    return simplejson.dumps(res)

@dajaxice_register
def unfollow(request, content_type_id, object_id):
    unfollowed = request.user.unfollow(content_type_id, object_id)
    res = {}
    if unfollowed:
        res['increment'] = -1
    else:
        res['increment'] = 0
    res['content_type_id'] = content_type_id
    res['object_id'] = object_id
    return simplejson.dumps(res)
