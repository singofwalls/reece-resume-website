"""
WSGI config for resumé project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings
import site

site.addsitedir("../.venv/lib/python3.10/site-packages")

import resume.monitor as monitor

monitor.start(interval=1.0)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume.settings')

if settings.DEBUG:
    import debugpy
    try:
        debugpy.log_to(settings.ATTACH_DEBUG_LOG_PATH)
    except RuntimeError:
        # This error occurs if the logging is already setup when attempting to launch
        #  wsgi.py -- such as when remoted into a virtual box repo hosting a live, Apache instance
        print("Debug a live instance with 'Attach to Django', not launch")
    debugpy.listen(("0.0.0.0", settings.ATTACH_DEBUG_PORT))

application = get_wsgi_application()
