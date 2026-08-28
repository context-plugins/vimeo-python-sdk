from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsSearchErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    NOT_AN_ADMIN = "not_an_admin"
    NOT_AN_ENTERPRISE = "not_an_enterprise"
    TEAM_NOT_FOUND = "team_not_found"
    NOT_ALLOWED = "not_allowed"
    INVALID_AUTH = "invalid_auth"
    INVALID_CURSOR = "invalid_cursor"
    INVALID_SEARCH_CHANNEL_TYPE = "invalid_search_channel_type"
    INVALID_SORT = "invalid_sort"
    INVALID_SORT_DIR = "invalid_sort_dir"

    __str__ = str.__str__


AdminConversationsSearchErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsSearchErrorEnum | str, open_enum_validator(AdminConversationsSearchErrorEnum)
]
