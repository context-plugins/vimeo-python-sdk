from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsGetConversationPrefsErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    NOT_AN_ADMIN = "not_an_admin"
    NOT_AN_ENTERPRISE = "not_an_enterprise"
    RESTRICTED_ACTION = "restricted_action"
    MISSING_SCOPE = "missing_scope"
    CHANNEL_NOT_FOUND = "channel_not_found"
    CHANNEL_TYPE_NOT_SUPPORTED = "channel_type_not_supported"
    COULD_NOT_GET_CONVERSATION_PREFS = "could_not_get_conversation_prefs"

    __str__ = str.__str__


AdminConversationsGetConversationPrefsErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsGetConversationPrefsErrorEnum | str,
    open_enum_validator(AdminConversationsGetConversationPrefsErrorEnum),
]
