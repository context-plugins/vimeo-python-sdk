from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Reason7(str, Enum):
    """The reason why the translation method is disabled.

    Option descriptions:
     * ``owner_account_blocked`` - The owner account is blocked due to billing issues.
     * ``owner_disabled_feature_group`` - The owner has disabled the feature group.
     * ``owner_payment_disabled`` - The owner account can't use the payments service.
     * ``transcript_status_does_not_exist`` - The video transcript doesn't exist."""

    OWNER_ACCOUNT_BLOCKED = "owner_account_blocked"
    OWNER_DISABLED_FEATURE_GROUP = "owner_disabled_feature_group"
    OWNER_PAYMENT_DISABLED = "owner_payment_disabled"
    TRANSCRIPT_STATUS_DOES_NOT_EXIST = "transcript_status_does_not_exist"

    __str__ = str.__str__


Reason7OrStr: TypeAlias = Annotated[Reason7 | str, open_enum_validator(Reason7)]
