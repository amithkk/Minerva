"""
WSGI config for Minerva project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

#  Copyright (c) 2018 - Amith K K
#  Released under the GNU GPLv3 License
#

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Minerva.settings')

application = get_wsgi_application()
