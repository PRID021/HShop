error_codes = {
    "unauthorized": {
        "common": 401000,
        "invalid": 401001,
        "login": {
            "blank": 401002,
            "token": {
                "failure": 401003,
            },
        },
    },
    "error_codes": {
        "common": 422000,
    },
}


error_messages = {
    "unauthorized": {
        "login": {
            "blank": "auth_email_and_password_required",
            "token": {
                "failure": "auth_cannot_generate_token",
            },
        },
        "common": "unauthorized",
    },
    "unprocessable_entity": {
        "login": {
            "invalid": "invalid_username_password",
        }
    },
}


messages = {
    "success": "success",
    "unprocessable_entity": {
        "common": "unprocessable_entity",
    },
}
