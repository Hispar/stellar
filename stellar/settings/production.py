"""Production settings and globals."""

from __future__ import absolute_import

from .base import *

# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# END DEBUG CONFIGURATION


# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# END EMAIL CONFIGURATION

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '/cloudsql/<your-app-id>:<your-cloudsql-instancename>',
        'NAME': '<your-database-name>',
        'USER': '<your-database-user>',
        'PASSWORD': '<your-database-password>',
    }
}
# END DATABASE CONFIGURATION

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
# SECRET_KEY = r"{{ secret_key }}"
SECRET_KEY = 't5js($qef5s1v^e#z5_aq7ahz-$ekj!gw(sf#tuz1(&)+30^m4'
# END SECRET CONFIGURATION