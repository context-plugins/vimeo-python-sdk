from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChatMeMessageErrorEnum(str, Enum):
    CHANNEL_NOT_FOUND = "channel_not_found"
    NOT_IN_CHANNEL = "not_in_channel"
    IS_ARCHIVED = "is_archived"
    MSG_TOO_LONG = "msg_too_long"
    NO_TEXT = "no_text"
    RATE_LIMITED = "rate_limited"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    TOKEN_REVOKED = "token_revoked"
    NO_PERMISSION = "no_permission"
    ORG_LOGIN_REQUIRED = "org_login_required"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_POST_TYPE = "invalid_post_type"
    MISSING_POST_TYPE = "missing_post_type"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    INVALID_JSON = "invalid_json"
    JSON_NOT_OBJECT = "json_not_object"
    REQUEST_TIMEOUT = "request_timeout"
    UPGRADE_REQUIRED = "upgrade_required"
    FATAL_ERROR = "fatal_error"

    __str__ = str.__str__


ChatMeMessageErrorEnumOrStr: TypeAlias = Annotated[
    ChatMeMessageErrorEnum | str, open_enum_validator(ChatMeMessageErrorEnum)
]
