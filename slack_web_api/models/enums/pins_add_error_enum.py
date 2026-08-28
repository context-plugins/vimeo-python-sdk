from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PinsAddErrorEnum(str, Enum):
    BAD_TIMESTAMP = "bad_timestamp"
    MESSAGE_NOT_FOUND = "message_not_found"
    CHANNEL_NOT_FOUND = "channel_not_found"
    NO_ITEM_SPECIFIED = "no_item_specified"
    ALREADY_PINNED = "already_pinned"
    PERMISSION_DENIED = "permission_denied"
    FILE_NOT_SHARED = "file_not_shared"
    NOT_PINNABLE = "not_pinnable"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    NO_PERMISSION = "no_permission"
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


PinsAddErrorEnumOrStr: TypeAlias = Annotated[PinsAddErrorEnum | str, open_enum_validator(PinsAddErrorEnum)]
