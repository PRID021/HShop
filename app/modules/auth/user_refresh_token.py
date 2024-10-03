from django.db import models

from app.modules.auth.client_user import ClientUser


class UserRefreshToken(models.Model):
    refresh_token = models.CharField(max_length=255)
    user = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "app_user_refresh_token"
