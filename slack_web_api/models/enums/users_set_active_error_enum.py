from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UsersSetActiveErrorEnum(str, Enum):
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    TOKEN_REVOKED = "token_revoked"
    NO_PERMISSION = "no_permission"
    ORG_LOGIN_REQUIRED = "org_login_required"
    EKM_ACCESS_DENIED = "ekm_access_denied"
    MISSING_SCOPE = "missing_scope"
    INVALID_ARGUMENTS = "invalid_arguments"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_POST_TYPE = "invalid_post_type"
    MISSING_POST_TYPE = "missing_post_type"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    REQUEST_TIMEOUT = "request_timeout"
    FATAL_ERROR = "fatal_error"
    INTERNAL_ERROR = "internal_error"

    __str__ = str.__str__


UsersSetActiveErrorEnumOrStr: TypeAlias = Annotated[
    UsersSetActiveErrorEnum | str, open_enum_validator(UsersSetActiveErrorEnum)
]
