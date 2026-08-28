from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FilesListErrorEnum(str, Enum):
    USER_NOT_FOUND = "user_not_found"
    UNKNOWN_TYPE = "unknown_type"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    NO_PERMISSION = "no_permission"
    USER_IS_BOT = "user_is_bot"
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


FilesListErrorEnumOrStr: TypeAlias = Annotated[FilesListErrorEnum | str, open_enum_validator(FilesListErrorEnum)]
