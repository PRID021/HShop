from django.contrib.auth.hashers import check_password

from app.modules.auth.models.client_user import ClientUser


def verify_password(email=None, password=None):
    try:
        user = ClientUser.objects.get(username=email)
        if check_password(password=password, encoded=user.password):
            return user
    except ClientUser.DoesNotExist:
        pass
    return None
