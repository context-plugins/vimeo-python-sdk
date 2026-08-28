from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChatUpdateErrorEnum(str, Enum):
    MESSAGE_NOT_FOUND = "message_not_found"
    CANT_UPDATE_MESSAGE = "cant_update_message"
    CHANNEL_NOT_FOUND = "channel_not_found"
    EDIT_WINDOW_CLOSED = "edit_window_closed"
    MSG_TOO_LONG = "msg_too_long"
    TOO_MANY_ATTACHMENTS = "too_many_attachments"
    RATE_LIMITED = "rate_limited"
    NO_TEXT = "no_text"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    TOKEN_REVOKED = "token_revoked"
    NO_PERMISSION = "no_permission"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_POST_TYPE = "invalid_post_type"
    MISSING_POST_TYPE = "missing_post_type"
    REQUEST_TIMEOUT = "request_timeout"
    INVALID_JSON = "invalid_json"
    JSON_NOT_OBJECT = "json_not_object"
    UPGRADE_REQUIRED = "upgrade_required"
    FATAL_ERROR = "fatal_error"
    IS_INACTIVE = "is_inactive"

    __str__ = str.__str__


ChatUpdateErrorEnumOrStr: TypeAlias = Annotated[ChatUpdateErrorEnum | str, open_enum_validator(ChatUpdateErrorEnum)]
