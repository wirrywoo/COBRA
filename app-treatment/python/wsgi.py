"""
WSGI config for demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import wandb

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python.settings')

wandb.init(project = 'cobe-platform', name = 'treatment', anonymous="allow")
application = get_wsgi_application()
