from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from app.modules.auth.models.user_refresh_token import UserRefreshToken
from app.utils.error_definition import error_codes, error_messages
from app.utils.response_request import response_err401, response_err422, response_ok
from app.utils.response_schema import success_response_scheme
from app.utils.verify_password import verify_password


class AuthViewSet(ViewSet):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        method="post",
        operation_description="Login with email and password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Email address"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Password"
                ),
            },
            required=["email", "password"],
        ),
        responses={
            200: success_response_scheme(
                message="Login Success",
                data={
                    "access_token": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
                    ),
                    "refresh_token": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example="dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4gZXhhbXBsZSB0aGF0IGlzIHZlcnkgbG9uZyBhbmQgY3J5cHRvZ3JhcGhpY2FsbHkgc2FmZQ==",
                    ),
                },
            ),
            400: openapi.Response(
                description="Invalid credentials",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "code": openapi.Schema(type=openapi.TYPE_INTEGER, example=400),
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING, example="Invalid credentials"
                        ),
                    },
                ),
            ),
        },
    )
    @action(
        detail=False,
        methods=["POST"],
        permission_classes=[AllowAny],
        authentication_classes=[],
    )
    def login(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
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
