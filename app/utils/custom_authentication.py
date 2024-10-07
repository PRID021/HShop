from rest_framework import authentication
from rest_framework.exceptions import APIException, ParseError
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import AccessToken

from app.modules.auth.models.client_user import ClientUser

from .response_request import response_err400, response_err401, response_err404
from .error_definition import error_codes,error_messages

class CustomAuthenticationFailed(APIException):
    def __init__(self, detail=None, code=None):
        if detail is not None:
            self.detail = detail
        if code is not None:
            self.code = code
        super().__init__(detail, code)


class CustomNotFound(APIException):
    def __init__(self, detail=None, code=None):
        if detail is not None:
            self.detail = detail
        if code is not None:
            self.code = code
        super().__init__(detail, code)


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = self.get_token_from_request(request)
        if not token:
            raise CustomAuthenticationFailed(
                error_messages["unauthorized"]["common"],
                code=error_codes["unauthorized"]["common"],
            )

        try:
            user_id = self.decode_token(token)
            user = ClientUser.objects.get(pk=user_id)
            return (user, None)
        except ClientUser.DoesNotExist:
            raise CustomNotFound(
                detail=error_messages["not_found"]["user"],
                code=error_codes["not_found"]["user"],
            )
        except (InvalidToken, TokenError) as e:
            raise CustomAuthenticationFailed(
                detail=error_messages["unauthorized"]["invalid"],
                code=error_codes["unauthorized"]["invalid"],
            )

    def get_token_from_request(self, request):
        auth_header = request.headers.get("Authorization", None)
        if auth_header and auth_header.startswith("Bearer "):
            return auth_header.split(" ")[1]
        return None

    def decode_token(self, token):
        try:
            decoded_token = AccessToken(token)
            user_id = decoded_token["user_id"]
            return user_id
        except Exception as e:
            raise InvalidToken


def custom_exception_handler(exc, context):
    if isinstance(exc, CustomAuthenticationFailed):
        return response_err401(code=exc.code, message=exc.detail)
    if isinstance(exc, CustomNotFound):
        return response_err404(code=exc.code, message=exc.detail)
    if isinstance(exc, ParseError):
        return response_err400()
    return None
