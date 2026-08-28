from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsSetConversationPrefsErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    NOT_AN_ADMIN = "not_an_admin"
    CHANNEL_NOT_FOUND = "channel_not_found"
    CHANNEL_TYPE_NOT_SUPPORTED = "channel_type_not_supported"
    RESTRICTED_ACTION = "restricted_action"
    MISSING_SCOPE = "missing_scope"
    COULD_NOT_SET_CHANNEL_PREF = "could_not_set_channel_pref"
    DEFAULT_ORG_WIDE_CHANNEL = "default_org_wide_channel"

    __str__ = str.__str__


AdminConversationsSetConversationPrefsErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsSetConversationPrefsErrorEnum | str,
    open_enum_validator(AdminConversationsSetConversationPrefsErrorEnum),
]
