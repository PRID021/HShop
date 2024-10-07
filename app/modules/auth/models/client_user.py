from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class ClientUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, default="")
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, null=True, blank=True)

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
        if not self.name:
            return f"{self.first_name} {self.last_name}".strip()
        return self.name

    def save(self, *args, **kwargs):
        # Set the name to first_name + last_name if name is not provided
        if not self.name:
            self.name = f"{self.first_name} {self.last_name}".strip()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Client Users"
        permissions = [
            ("can_vote", "Can vote for a choice"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        ]
