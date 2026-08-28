from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DialogOpenErrorEnum(str, Enum):
    VALIDATION_ERRORS = "validation_errors"
    MISSING_TRIGGER = "missing_trigger"
    MISSING_DIALOG = "missing_dialog"
    TRIGGER_EXCHANGED = "trigger_exchanged"
    TRIGGER_EXPIRED = "trigger_expired"
    INVALID_TRIGGER = "invalid_trigger"
    APP_MISSING_ACTION_URL = "app_missing_action_url"
    CANNOT_CREATE_DIALOG = "cannot_create_dialog"
    FAILED_SENDING_DIALOG = "failed_sending_dialog"
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


DialogOpenErrorEnumOrStr: TypeAlias = Annotated[DialogOpenErrorEnum | str, open_enum_validator(DialogOpenErrorEnum)]
