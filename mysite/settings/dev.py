from .base import *

# Development settings
DEBUG = True

SECRET_KEY = "django-insecure-$p_)6&ijobirr1r%n+8f_o=(+6sx49p8i*6d@_j)u(rp2vr90+"

ALLOWED_HOSTS = ["*"]

# Database settings (can be SQLite for development)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "databases" / "default_db.sqlite3",
    },
    "auth": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "databases" / "auth_db.sqlite3",
    },
    "polls": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "databases" / "pools_db.sqlite3",
    },
    "askservice": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "databases" / "askservice_db.sqlite3",
    },
}


# Other development-specific settings
INSTALLED_APPS += ["debug_toolbar"]  # Example: Adding debug toolbar for development


MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = [
    "127.0.0.1",
]
