from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "tiendadb",
        'USER': "postgres",
        'PASSWORD': "12345678",
        'HOST': "localhost",
        'PORT': '5432',
    }
}


