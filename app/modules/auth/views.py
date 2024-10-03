from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from app.modules.auth.client_user import ClientUser
from app.modules.auth.user_refresh_token import UserRefreshToken
from app.utils.error_definition import error_codes, error_messages, messages
from app.utils.response_request import response_err401, response_err422, response_ok
from app.utils.verify_password import verify_password


class AuthViewSet(ViewSet):

    @action(
        detail=False,
        methods=["POST"],
        permission_classes=[AllowAny],
        authentication_classes=[],
    )
    def login(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or password:
            return response_err401(
                code=error_messages["unauthorized"]["login"]["blank"]
            )
        user = verify_password(email=email, password=password)

        if not user:
            return response_err422(
                errors={
                    "password": [
                        error_messages["unprocessable_entity"]["login"]["invalid"]
                    ]
                }
            )
        # Create Token by JWT
        refresh_token: RefreshToken = RefreshToken.for_user(user)
        if not refresh_token:
            return response_err401(
                message=error_messages["unauthorized"]["login"]["token"]["failure"],
                code=error_codes["unauthorized"]["login"]["token"]["failure"],
            )

        UserRefreshToken.objects.create(
            refresh_token=str(refresh_token),
            user=user,
        )
        result = {
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token),
        }
        return response_ok(result)
