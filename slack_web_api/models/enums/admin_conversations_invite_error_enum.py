from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsInviteErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    CHANNEL_NOT_FOUND = "channel_not_found"
    CHANNEL_TYPE_NOT_SUPPORTED = "channel_type_not_supported"
    DEFAULT_ORG_WIDE_CHANNEL = "default_org_wide_channel"
    RESTRICTED_ACTION = "restricted_action"
    USER_MUST_BE_ADMIN = "user_must_be_admin"
    FAILED_FOR_SOME_USERS = "failed_for_some_users"

    __str__ = str.__str__


AdminConversationsInviteErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsInviteErrorEnum | str, open_enum_validator(AdminConversationsInviteErrorEnum)
]
