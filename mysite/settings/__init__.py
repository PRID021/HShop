import os

if os.getenv("DJANGO_ENV") == "production":
    from .prod import *
elif os.getenv("DJANGO_ENV") == "test":
    from .test import *
else:
    from .dev import *
