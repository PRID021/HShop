import os

from celery import Celery
from django.conf import settings

# Get the DJANGO_ENV environment variable (default to 'dev')
environment = os.getenv("DJANGO_ENV", "dev")

# Map the environment to the corresponding settings file
if environment == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.prod")
elif environment == "test":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.test")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.dev")

app = Celery("app")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
