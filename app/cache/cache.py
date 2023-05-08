import json

from django.core.cache import cache


class Cache:
    @staticmethod
    def set(key, data):
        cache.set(key=key, value=data)

    @staticmethod
    def delete(key):
        cache.delete(key=key)

    @staticmethod
    def get(key):
        return cache.get(key=key)

    @staticmethod
    def set_json(key, data):
        cache.set(key=key, value=json.dumps(data))

    @staticmethod
    def get_json(key, default=None):
        data = cache.get(key=key)

        if data is not None:
            return json.loads(data)
        elif default is not None:
            return default

        return None
