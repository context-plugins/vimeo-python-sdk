from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConversationsUnarchiveErrorEnum(str, Enum):
    METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE = "method_not_supported_for_channel_type"
    MISSING_SCOPE = "missing_scope"
    CHANNEL_NOT_FOUND = "channel_not_found"
    NOT_ARCHIVED = "not_archived"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    USER_IS_BOT = "user_is_bot"
    USER_IS_RESTRICTED = "user_is_restricted"
    USER_IS_ULTRA_RESTRICTED = "user_is_ultra_restricted"
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
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    MISSING_CHARSET = "missing_charset"
    SUPERFLUOUS_CHARSET = "superfluous_charset"

    __str__ = str.__str__


ConversationsUnarchiveErrorEnumOrStr: TypeAlias = Annotated[
    ConversationsUnarchiveErrorEnum | str, open_enum_validator(ConversationsUnarchiveErrorEnum)
]
