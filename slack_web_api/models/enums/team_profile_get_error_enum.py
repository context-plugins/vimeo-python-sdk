from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TeamProfileGetErrorEnum(str, Enum):
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    NO_PERMISSION = "no_permission"
    USER_IS_BOT = "user_is_bot"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_POST_TYP = "invalid_post_typ"
    MISSING_POST_TYPE = "missing_post_type"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    INVALID_JSON = "invalid_json"
    JSON_NOT_OBJECT = "json_not_object"
    REQUEST_TIMEOU = "request_timeou"
    UPGRADE_REQUIRED = "upgrade_required"

    __str__ = str.__str__


TeamProfileGetErrorEnumOrStr: TypeAlias = Annotated[
    TeamProfileGetErrorEnum | str, open_enum_validator(TeamProfileGetErrorEnum)
]
