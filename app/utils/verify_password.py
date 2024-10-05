

from app.modules.auth.models.client_user import ClientUser
from django.contrib.auth.hashers import check_password 

def verify_password(email= None, password= None):
    try:
        user = ClientUser.objects.get(email=email)
        if check_password(password=password,encoded=user.password):
            return user
    except ClientUser.DoesNotExist:
        pass
    return None