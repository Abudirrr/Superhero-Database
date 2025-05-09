import os
import sys

# ✅ Path to your Django project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ✅ Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hireahero.settings")

# ✅ Get WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
