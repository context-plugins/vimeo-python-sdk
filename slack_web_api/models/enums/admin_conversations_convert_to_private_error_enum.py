from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdminConversationsConvertToPrivateErrorEnum(str, Enum):
    FEATURE_NOT_ENABLED = "feature_not_enabled"
    RESTRICTED_ACTION = "restricted_action"
    NAME_TAKEN = "name_taken"
    CHANNEL_NOT_FOUND = "channel_not_found"
    CHANNEL_TYPE_NOT_SUPPORTED = "channel_type_not_supported"
    DEFAULT_ORG_WIDE_CHANNEL = "default_org_wide_channel"
    METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE = "method_not_supported_for_channel_type"
    COULD_NOT_CONVERT_CHANNEL = "could_not_convert_channel"
    EXTERNAL_CHANNEL_MIGRATING = "external_channel_migrating"

    __str__ = str.__str__


AdminConversationsConvertToPrivateErrorEnumOrStr: TypeAlias = Annotated[
    AdminConversationsConvertToPrivateErrorEnum | str, open_enum_validator(AdminConversationsConvertToPrivateErrorEnum)
]
