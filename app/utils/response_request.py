from rest_framework import status
from .error_definition import messages
from django.http import JsonResponse


def response_ok(data=None, meta={}):
    result = {"code": status.HTTP_200_OK, "message": messages["success"]}
    if meta:
        result.update({"meta": meta})
    if data is not None:
        result.update({"data": data})
    return JsonResponse(result, status=status.HTTP_200_OK)
