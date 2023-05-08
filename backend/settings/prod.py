from .base import *

DEBUG = False

SECRET_KEY = 'QfPl(ikiTB8%7-oB_^WjJN8%PXcPGZ,}^zz69nPk!ENN^`&h:c;!8;yVGz'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'creditfair',
        'USER': 'creditfair',
        'HOST': 'prod_host',
        'PASSWORD': 'prod_password',
    },
}

