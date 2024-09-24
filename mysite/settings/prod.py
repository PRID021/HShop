from .base import *

# Production settings
DEBUG = False

SECRET_KEY = "your-production-secret-key"

ALLOWED_HOSTS = ["your-domain.com"]

# Database settings (use PostgreSQL or another production-ready DB)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "your_db_name",
        "USER": "your_db_user",
        "PASSWORD": "your_db_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
