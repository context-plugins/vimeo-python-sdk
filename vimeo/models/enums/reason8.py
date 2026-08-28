from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Reason8(str, Enum):
    """The reason why the translation method is disabled.

    Option descriptions:
     * ``language_not_supported`` - The video language isn't supported.
     * ``owner_account_blocked`` - The owner account is blocked due to billing issues.
     * ``owner_disabled_feature_group`` - The owner has disabled the feature group.
     * ``video_too_long`` - The video is too long."""

    LANGUAGE_NOT_SUPPORTED = "language_not_supported"
    OWNER_ACCOUNT_BLOCKED = "owner_account_blocked"
    OWNER_DISABLED_FEATURE_GROUP = "owner_disabled_feature_group"
    VIDEO_TOO_LONG = "video_too_long"

    __str__ = str.__str__


Reason8OrStr: TypeAlias = Annotated[Reason8 | str, open_enum_validator(Reason8)]
