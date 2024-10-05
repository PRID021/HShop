from .base import *

# Development settings
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Other development-specific settings
INSTALLED_APPS += ["debug_toolbar"]  # Example: Adding debug toolbar for development


MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = [
    "127.0.0.1",
]



