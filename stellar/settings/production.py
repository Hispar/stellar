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
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/stellar-1219:stellartest1',
            'NAME': 'stellar',
            'USER': 'stellar_user',
            'PASSWPORD': 'stellar_pass'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '<your-database-name>',
            'USER': '<your-database-user>',
            'PASSWORD': '<your-database-password>',
            'HOST': '<your-database-host>',
            'PORT': '3306',
        }
    }
# END DATABASE CONFIGURATION

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
# SECRET_KEY = r"{{ secret_key }}"
SECRET_KEY = 't5js($qef5s1v^e#z5_aq7ahz-$ekj!gw(sf#tuz1(&)+30^m4'
# END SECRET CONFIGURATION