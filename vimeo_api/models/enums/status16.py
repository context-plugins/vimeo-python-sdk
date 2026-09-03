from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status16(str, Enum):
    """The status of the subscription.

    Option descriptions:
     * ``SUBSCRIPTION_STATUS_ACTIVE`` - The subscription is active.
     * ``SUBSCRIPTION_STATUS_CANCELLED`` - The subscription is canceled.
     * ``SUBSCRIPTION_STATUS_DRAFT`` - The subscription is a draft.
     * ``SUBSCRIPTION_STATUS_EXPIRED`` - The subscription is expired.
     * ``SUBSCRIPTION_STATUS_PAUSED`` - The subscription is paused.
     * ``SUBSCRIPTION_STATUS_PENDING_ACCEPTANCE`` - The subscription is pending acceptance.
     * ``SUBSCRIPTION_STATUS_PENDING_ACTIVATION`` - The subscription is pending activation.
     * ``SUBSCRIPTION_STATUS_UNSPECIFIED`` - The subscription status is unspecified."""

    SUBSCRIPTION_STATUS_ACTIVE = "SUBSCRIPTION_STATUS_ACTIVE"
    SUBSCRIPTION_STATUS_CANCELLED = "SUBSCRIPTION_STATUS_CANCELLED"
    SUBSCRIPTION_STATUS_DRAFT = "SUBSCRIPTION_STATUS_DRAFT"
    SUBSCRIPTION_STATUS_EXPIRED = "SUBSCRIPTION_STATUS_EXPIRED"
    SUBSCRIPTION_STATUS_PAUSED = "SUBSCRIPTION_STATUS_PAUSED"
    SUBSCRIPTION_STATUS_PENDING_ACCEPTANCE = "SUBSCRIPTION_STATUS_PENDING_ACCEPTANCE"
    SUBSCRIPTION_STATUS_PENDING_ACTIVATION = "SUBSCRIPTION_STATUS_PENDING_ACTIVATION"
    SUBSCRIPTION_STATUS_UNSPECIFIED = "SUBSCRIPTION_STATUS_UNSPECIFIED"

    __str__ = str.__str__


Status16OrStr: TypeAlias = Annotated[Status16 | str, open_enum_validator(Status16)]
