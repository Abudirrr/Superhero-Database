"""
WSGI config for hireahero project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hireahero.settings")

application = get_wsgi_application()

# ✅ Enable WhiteNoise for serving static files in production (Render)
application = WhiteNoise(application)
