from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status import StatusOrStr


class Billing(SdkBaseModel):
    """Information about the authenticated user's subscription billing."""

    status: StatusOrStr
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


class BillingDict(TypedDict):
    status: StatusOrStr
