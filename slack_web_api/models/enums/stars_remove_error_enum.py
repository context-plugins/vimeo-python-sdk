from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StarsRemoveErrorEnum(str, Enum):
    BAD_TIMESTAMP = "bad_timestamp"
    MESSAGE_NOT_FOUND = "message_not_found"
    FILE_NOT_FOUND = "file_not_found"
    FILE_COMMENT_NOT_FOUND = "file_comment_not_found"
    CHANNEL_NOT_FOUND = "channel_not_found"
    NO_ITEM_SPECIFIED = "no_item_specified"
    NOT_STARRED = "not_starred"
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


StarsRemoveErrorEnumOrStr: TypeAlias = Annotated[StarsRemoveErrorEnum | str, open_enum_validator(StarsRemoveErrorEnum)]
