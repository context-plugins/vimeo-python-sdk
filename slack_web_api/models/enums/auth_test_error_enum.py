from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthTestErrorEnum(str, Enum):
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    TOKEN_REVOKED = "token_revoked"
    ACCOUNT_INACTIVE = "account_inactive"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_POST_TYPE = "invalid_post_type"
    MISSING_POST_TYPE = "missing_post_type"
    INVALID_JSON = "invalid_json"
    JSON_NOT_OBJECT = "json_not_object"
    REQUEST_TIMEOUT = "request_timeout"
    UPGRADE_REQUIRED = "upgrade_required"

    __str__ = str.__str__


AuthTestErrorEnumOrStr: TypeAlias = Annotated[AuthTestErrorEnum | str, open_enum_validator(AuthTestErrorEnum)]
