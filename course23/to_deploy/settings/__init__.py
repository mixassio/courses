# -*- coding: utf-8 -*-

from split_settings.tools import optional, include
from components import CONFIG

# To change settings file:
# `python manage.py runserver --settings=to_deployother_settings`

if CONFIG['DJANGO_SETTINGS_MODULE'] == 'to_deploy.settings':
    testing = bool(CONFIG['_DJANGO_TESTING'])

    base_settings = [
        'components/common.py',
        # 'components/constants.py',
        # 'components/queues.py',
    ]

    if not testing:
        settings = base_settings + [
            'environments/production.py',
            optional('environments/development.py'),
        ]

    else:
        settings = base_settings + [
            'environments/testing.py',
        ]

    # Include settings for the current env:
    include(*settings, scope=globals())
