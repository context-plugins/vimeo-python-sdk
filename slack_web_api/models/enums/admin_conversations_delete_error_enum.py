from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsDeleteErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    NOT_AN_ADMIN = "not_an_admin"
    CHANNEL_NOT_FOUND = "channel_not_found"
    CHANNEL_TYPE_NOT_SUPPORTED = "channel_type_not_supported"
    DEFAULT_ORG_WIDE_CHANNEL = "default_org_wide_channel"
    RESTRICTED_ACTION = "restricted_action"
    COULD_NOT_DELETE_CHANNEL = "could_not_delete_channel"
    MISSING_SCOPE = "missing_scope"

    __str__ = str.__str__


AdminConversationsDeleteErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsDeleteErrorEnum | str, open_enum_validator(AdminConversationsDeleteErrorEnum)
]
