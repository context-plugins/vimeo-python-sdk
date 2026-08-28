from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConversationsMarkErrorEnum(str, Enum):
    METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE = "method_not_supported_for_channel_type"
    MISSING_SCOPE = "missing_scope"
    CHANNEL_NOT_FOUND = "channel_not_found"
    INVALID_TIMESTAMP = "invalid_timestamp"
    NOT_IN_CHANNEL = "not_in_channel"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
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
    NOT_ALLOWED_TOKEN_TYPE = "not_allowed_token_type"

    __str__ = str.__str__


ConversationsMarkErrorEnumOrStr: TypeAlias = Annotated[
    ConversationsMarkErrorEnum | str, open_enum_validator(ConversationsMarkErrorEnum)
]
