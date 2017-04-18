# -*- coding: utf-8 -*-

"""
This file determines all the settings that must define the testing server.
Basically it copies the development settings. It is included in VCS.

SECURITY WARNING: don't run with debug turned on in production!
"""

# Mind the proper import, use the right module!
from to_deploy.settings.components.common import (
    TEMPLATES,
    BASE_DIR,
)

import os

# Setting the development status:

DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

FRONTEND_DEBUG = True

ALLOWED_HOSTS = []

# Network security and SSL:

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
    # '0.0.0.0',

    # Uncomment next line and run
    # 'runserver 0.0.0.0:8000' for production test:
    # '192.168.(insert).(yours)'
]


# Static files:
# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'bitcoins', 'static'),

    # Adding frontend package managers in development:
    # os.path.join(BASE_DIR, 'node_modules'),
    os.path.join(BASE_DIR, 'bower_components'),
)

# Adding STATIC_ROOT to collect static files via 'collectstatic'.
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# Media files root:

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s "
                      "[%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'server.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'server': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
