"""
WSGI config for chat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import django
import socketio

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')
django.setup()

application = get_wsgi_application()

from app.message.views import sio
application = socketio.WSGIApp(sio, application)
