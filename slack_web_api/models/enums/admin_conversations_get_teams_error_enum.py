from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsGetTeamsErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    CHANNEL_NOT_FOUND = "channel_not_found"
    CHANNEL_TYPE_NOT_SUPPORTED = "channel_type_not_supported"
    UNSUPPORTED_TEAM_TYPE = "unsupported_team_type"
    RESTRICTED_ACTION = "restricted_action"
    COULD_NOT_GET_TEAMS = "could_not_get_teams"
    INVALID_CURSOR = "invalid_cursor"
    INVALID_LIMIT = "invalid_limit"

    __str__ = str.__str__


AdminConversationsGetTeamsErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsGetTeamsErrorEnum | str, open_enum_validator(AdminConversationsGetTeamsErrorEnum)
]
