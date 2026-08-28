from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsArchiveErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    CHANNEL_NOT_FOUND = "channel_not_found"
    CHANNEL_TYPE_NOT_SUPPORTED = "channel_type_not_supported"
    DEFAULT_ORG_WIDE_CHANNEL = "default_org_wide_channel"
    ALREADY_ARCHIVED = "already_archived"
    CANT_ARCHIVE_GENERAL = "cant_archive_general"
    RESTRICTED_ACTION = "restricted_action"
    COULD_NOT_ARCHIVE_CHANNEL = "could_not_archive_channel"

    __str__ = str.__str__


AdminConversationsArchiveErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsArchiveErrorEnum | str, open_enum_validator(AdminConversationsArchiveErrorEnum)
]
