from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.request import Request

class AuthViewSet(ViewSet):
    
    def login(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
