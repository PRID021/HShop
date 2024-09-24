#!/usr/bin/env python
import os
import sys


def main():
    """Run administrative tasks."""
    # Determine which settings file to use based on environment variable
    environment = os.getenv("DJANGO_ENV", "dev")  # Default to 'dev' if not set

    # Map the environment to the corresponding settings file
    if environment == "production":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.prod")
    elif environment == "test":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.test")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your "
            "PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
