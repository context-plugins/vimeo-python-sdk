from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsDisconnectSharedErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    NOT_AN_ADMIN = "not_an_admin"
    NOT_AN_ENTERPRISE = "not_an_enterprise"
    CHANNEL_NOT_FOUND = "channel_not_found"
    NOT_SUPPORTED = "not_supported"
    TEAM_NOT_FOUND = "team_not_found"
    RESTRICTED_ACTION = "restricted_action"
    MISSING_SCOPE = "missing_scope"
    LEAVING_TEAM_NOT_IN_CHANNEL = "leaving_team_not_in_channel"
    NO_TEAMS_TO_DISCONNECT = "no_teams_to_disconnect"
    LEAVING_TEAM_REQUIRED = "leaving_team_required"
    CANNOT_KICK_TEAM = "cannot_kick_team"
    CANNOT_KICK_HOME_TEAM = "cannot_kick_home_team"

    __str__ = str.__str__


AdminConversationsDisconnectSharedErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsDisconnectSharedErrorEnum | str, open_enum_validator(AdminConversationsDisconnectSharedErrorEnum)
]
