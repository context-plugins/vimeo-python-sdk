from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChatDeleteErrorEnum(str, Enum):
    MESSAGE_NOT_FOUND = "message_not_found"
    CHANNEL_NOT_FOUND = "channel_not_found"
    CANT_DELETE_MESSAGE = "cant_delete_message"
    COMPLIANCE_EXPORTS_PREVENT_DELETION = "compliance_exports_prevent_deletion"
    NOT_AUTHED = "not_authed"
    INVALID_AUTH = "invalid_auth"
    ACCOUNT_INACTIVE = "account_inactive"
    TOKEN_REVOKED = "token_revoked"
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
    FATAL_ERROR = "fatal_error"

    __str__ = str.__str__


ChatDeleteErrorEnumOrStr: TypeAlias = Annotated[ChatDeleteErrorEnum | str, open_enum_validator(ChatDeleteErrorEnum)]
