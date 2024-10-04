from drf_yasg import openapi


def success_response_scheme(**kwargs) -> openapi.Response:
    description = kwargs.get("description", "Success")
    code = kwargs.get("code", 200)
    message = kwargs.get("message", "Success")
    data = kwargs.get("data", None)
    meta = kwargs.get("meta", None)

    properties = {
        "code": openapi.Schema(type=openapi.TYPE_INTEGER, example=code),
        "message": openapi.Schema(type=openapi.TYPE_STRING, example=message),
    }
    if meta is not None:
        properties["meta"] = openapi.Schema(type=openapi.TYPE_STRING, example=meta)

    if data is not None:
        properties["data"] = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=data,
        )

    return openapi.Response(
        description=description,
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=properties,
        ),
    )
