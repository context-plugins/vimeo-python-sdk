from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsCreateErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    NAME_TAKEN = "name_taken"
    RESTRICTED_ACTION = "restricted_action"
    TEAM_NOT_FOUND = "team_not_found"
    INVALID_TEAM = "invalid_team"
    INVALID_NAME = "invalid_name"
    COULD_NOT_CREATE_CHANNEL = "could_not_create_channel"
    TEAM_ID_OR_ORG_REQUIRED = "team_id_or_org_required"

    __str__ = str.__str__


AdminConversationsCreateErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsCreateErrorEnum | str, open_enum_validator(AdminConversationsCreateErrorEnum)
]
