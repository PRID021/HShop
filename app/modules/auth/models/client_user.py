from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class ClientUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, default="anonymus")
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Override the default related names for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        related_name="clientuser_set",  # Change this to avoid clashes
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="clientuser_set",  # Change this to avoid clashes
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Client Users"
        permissions = [
            ("can_vote", "Can vote for a choice"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        ]
