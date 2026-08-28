from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChatPostMessageErrorEnum(str, Enum):
    CHANNEL_NOT_FOUND = "channel_not_found"
    NOT_IN_CHANNEL = "not_in_channel"
    IS_ARCHIVED = "is_archived"
    MSG_TOO_LONG = "msg_too_long"
    NO_TEXT = "no_text"
    TOO_MANY_ATTACHMENTS = "too_many_attachments"
    RATE_LIMITED = "rate_limited"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_POST_TYPE = "invalid_post_type"
    MISSING_POST_TYPE = "missing_post_type"

    __str__ = str.__str__


ChatPostMessageErrorEnumOrStr: TypeAlias = Annotated[
    ChatPostMessageErrorEnum | str, open_enum_validator(ChatPostMessageErrorEnum)
]
