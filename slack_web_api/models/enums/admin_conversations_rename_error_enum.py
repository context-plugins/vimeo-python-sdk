from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsRenameErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    CHANNEL_NOT_FOUND = "channel_not_found"
    CHANNEL_TYPE_NOT_SUPPORTED = "channel_type_not_supported"
    RESTRICTED_ACTION = "restricted_action"
    COULD_NOT_RENAME_CHANNEL = "could_not_rename_channel"
    DEFAULT_ORG_WIDE_CHANNEL = "default_org_wide_channel"
    NAME_TAKEN = "name_taken"

    __str__ = str.__str__


AdminConversationsRenameErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsRenameErrorEnum | str, open_enum_validator(AdminConversationsRenameErrorEnum)
]
