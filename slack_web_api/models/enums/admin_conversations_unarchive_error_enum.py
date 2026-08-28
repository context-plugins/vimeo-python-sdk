from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsUnarchiveErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    CHANNEL_NOT_FOUND = "channel_not_found"
    CHANNEL_NOT_ARCHIVED = "channel_not_archived"
    CHANNEL_TYPE_NOT_SUPPORTED = "channel_type_not_supported"
    RESTRICTED_ACTION = "restricted_action"
    COULD_NOT_UNARCHIVE_CHANNEL = "could_not_unarchive_channel"
    DEFAULT_ORG_WIDE_CHANNEL = "default_org_wide_channel"
    MISSING_SCOPE = "missing_scope"

    __str__ = str.__str__


AdminConversationsUnarchiveErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsUnarchiveErrorEnum | str, open_enum_validator(AdminConversationsUnarchiveErrorEnum)
]
