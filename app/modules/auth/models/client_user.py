from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class ClientUser(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.username
