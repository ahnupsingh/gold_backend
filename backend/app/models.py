import uuid

from django.db import models

from django.contrib.auth.models import AbstractUser


def get_24_char_uuid():
    uid = uuid.uuid4().hex
    for i in range(0, 8):
        uid = uid[:i] + uid[i + 1:]
    return uid.upper()


class User(AbstractUser):
    id = models.CharField(max_length=100, primary_key=True, default=get_24_char_uuid)
    phone_number = models.CharField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return self.username
