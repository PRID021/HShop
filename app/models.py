from .modules.auth.models.client_user import (
    ClientUser,
)  # Fix "AUTH_USER_MODEL" django.core.exceptions.ImproperlyConfigured
from .modules.polls.models.choice import Choice
from .modules.polls.models.question import Question

# Makemigrations could detect changes in app models but migrate couldn't find them in custom models folder.
# https://www.reddit.com/r/django/comments/x27iho/comment/imkgewb/
__all__ = ["Question", "Choice", "ClientUser"]
