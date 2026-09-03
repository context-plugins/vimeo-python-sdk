from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status(str, Enum):
    """The billing status of the subscription.

    Option descriptions:
     * ``active`` - The subscription is in good standing and will renew automatically on the renewal date.
     * ``cancelled`` - The subscription is or will become inactive on the expiration date and won't renew automatically.
     * ``grace_period`` - The subscription has passed the expiration date but is still active. The automatic renewal
            charge is being retried.
     * ``none`` - The subscription doesn't exist. A subscription in this state can be considered as erroring.
     * ``on_hold`` - The subscription's automatic renewal payment has failed, and the grace period has expired.
     * ``pending`` - The status of the subscription is pending. A subscription in this state can be considered as
            erroring."""

    ACTIVE = "active"
    CANCELLED = "cancelled"
    GRACE_PERIOD = "grace_period"
    NONE = "none"
    ON_HOLD = "on_hold"
    PENDING = "pending"

    __str__ = str.__str__


StatusOrStr: TypeAlias = Annotated[Status | str, open_enum_validator(Status)]
