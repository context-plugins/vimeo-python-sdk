from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConversationsSetPurposeErrorEnum(str, Enum):
    METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE = "method_not_supported_for_channel_type"
    MISSING_SCOPE = "missing_scope"
    CHANNEL_NOT_FOUND = "channel_not_found"
    NOT_IN_CHANNEL = "not_in_channel"
    IS_ARCHIVED = "is_archived"
    TOO_LONG = "too_long"
    USER_IS_RESTRICTED = "user_is_restricted"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
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

    __str__ = str.__str__


ConversationsSetPurposeErrorEnumOrStr: TypeAlias = Annotated[
    ConversationsSetPurposeErrorEnum | str, open_enum_validator(ConversationsSetPurposeErrorEnum)
]
