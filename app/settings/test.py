from .base import *

# Testing settings
DEBUG = False

ALLOWED_HOSTS = []

# Disable password validators for faster tests
AUTH_PASSWORD_VALIDATORS = []

# Configure a test email backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
