from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChatScheduleMessageErrorEnum(str, Enum):
    INVALID_TIME = "invalid_time"
    TIME_IN_PAST = "time_in_past"
    TIME_TOO_FAR = "time_too_far"
    CHANNEL_NOT_FOUND = "channel_not_found"
    NOT_IN_CHANNEL = "not_in_channel"
    IS_ARCHIVED = "is_archived"
    MSG_TOO_LONG = "msg_too_long"
    NO_TEXT = "no_text"
    RESTRICTED_ACTION = "restricted_action"
    RESTRICTED_ACTION_READ_ONLY_CHANNEL = "restricted_action_read_only_channel"
    RESTRICTED_ACTION_THREAD_ONLY_CHANNEL = "restricted_action_thread_only_channel"
    RESTRICTED_ACTION_NON_THREADABLE_CHANNEL = "restricted_action_non_threadable_channel"
    TOO_MANY_ATTACHMENTS = "too_many_attachments"
    RATE_LIMITED = "rate_limited"
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
    INVALID_JSON = "invalid_json"
    JSON_NOT_OBJECT = "json_not_object"
    REQUEST_TIMEOUT = "request_timeout"
    UPGRADE_REQUIRED = "upgrade_required"
    FATAL_ERROR = "fatal_error"

    __str__ = str.__str__


ChatScheduleMessageErrorEnumOrStr: TypeAlias = Annotated[
    ChatScheduleMessageErrorEnum | str, open_enum_validator(ChatScheduleMessageErrorEnum)
]
