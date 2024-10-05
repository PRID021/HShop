from .base import *

# Production settings
DEBUG = False

ALLOWED_HOSTS = ["your-domain.com"]

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"


