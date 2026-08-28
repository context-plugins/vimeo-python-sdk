from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PinsRemoveErrorEnum(str, Enum):
    BAD_TIMESTAMP = "bad_timestamp"
    FILE_NOT_FOUND = "file_not_found"
    FILE_COMMENT_NOT_FOUND = "file_comment_not_found"
    MESSAGE_NOT_FOUND = "message_not_found"
    NO_ITEM_SPECIFIED = "no_item_specified"
    NOT_PINNED = "not_pinned"
    PERMISSION_DENIED = "permission_denied"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    NO_PERMISSION = "no_permission"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_POST_TYP = "invalid_post_typ"
    MISSING_POST_TYP = "missing_post_typ"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    INVALID_JSON = "invalid_json"
    JSON_NOT_OBJECT = "json_not_object"
    REQUEST_TIMEOU = "request_timeou"
    UPGRADE_REQUIRED = "upgrade_required"

    __str__ = str.__str__


PinsRemoveErrorEnumOrStr: TypeAlias = Annotated[PinsRemoveErrorEnum | str, open_enum_validator(PinsRemoveErrorEnum)]
