from .auth_views import *
from .dashboard_views import *
from .hero_views import *
from .cart_views import *
from .profile_views import *
from .static_views import *

# Ensure signals are registered
import main.signals
