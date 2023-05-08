import uuid

from app.api.api import STATUS_SUCCESS


def is_status_failed(status):
    return status != STATUS_SUCCESS


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def get_char_uuid(length):
    uid = uuid.uuid4().hex
    return uid[:length]
