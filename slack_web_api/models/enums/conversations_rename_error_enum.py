from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConversationsRenameErrorEnum(str, Enum):
    USER_IS_RESTRICTED = "user_is_restricted"
    METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE = "method_not_supported_for_channel_type"
    MISSING_SCOPE = "missing_scope"
    CHANNEL_NOT_FOUND = "channel_not_found"
    NOT_IN_CHANNEL = "not_in_channel"
    NOT_AUTHORIZED = "not_authorized"
    INVALID_NAME = "invalid_name"
    NAME_TAKEN = "name_taken"
    INVALID_NAME_REQUIRED = "invalid_name_required"
    INVALID_NAME_PUNCTUATION = "invalid_name_punctuation"
    INVALID_NAME_MAXLENGTH = "invalid_name_maxlength"
    INVALID_NAME_SPECIALS = "invalid_name_specials"
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

    __str__ = str.__str__


ConversationsRenameErrorEnumOrStr: TypeAlias = Annotated[
    ConversationsRenameErrorEnum | str, open_enum_validator(ConversationsRenameErrorEnum)
]
