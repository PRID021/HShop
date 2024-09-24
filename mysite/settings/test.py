from .base import *

# Testing settings
DEBUG = False

SECRET_KEY = "test-secret-key"

ALLOWED_HOSTS = []

# Use an in-memory SQLite database for faster tests
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Disable password validators for faster tests
AUTH_PASSWORD_VALIDATORS = []

# Configure a test email backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
