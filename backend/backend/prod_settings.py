from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database',
        'USER': 'database_user',
        'HOST': 'prod_host',
        'PASSWORD': 'prod_password',
    },
}