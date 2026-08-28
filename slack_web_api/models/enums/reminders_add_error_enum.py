from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RemindersAddErrorEnum(str, Enum):
    CANNOT_PARSE = "cannot_parse"
    USER_NOT_FOUND = "user_not_found"
    CANNOT_ADD_BOT = "cannot_add_bot"
    CANNOT_ADD_SLACKBOT = "cannot_add_slackbot"
    CANNOT_ADD_OTHERS = "cannot_add_others"
    CANNOT_ADD_OTHERS_RECURRING = "cannot_add_others_recurring"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    TOKEN_REVOKED = "token_revoked"
    NO_PERMISSION = "no_permission"
    ORG_LOGIN_REQUIRED = "org_login_required"
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
    FATAL_ERROR = "fatal_error"

    __str__ = str.__str__


RemindersAddErrorEnumOrStr: TypeAlias = Annotated[
    RemindersAddErrorEnum | str, open_enum_validator(RemindersAddErrorEnum)
]
