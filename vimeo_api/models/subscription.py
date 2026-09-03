from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status16 import Status16OrStr
from .plan import Plan, PlanDict


class Subscription(SdkBaseModel):
    account_id: str
    """The ID of the account."""

    auto_renew: bool
    """Whether the subscription is set to renew automatically."""

    can_renew_now: bool
    """Whether the user can extend their subscription's expiration date by an additional billing period for the same
    product tier."""

    created_at: str
    """The time in ISO 8601 format when the subscription was created."""

    disabled_at: Optional[str] = UNSET
    """The time in ISO 8601 format when the subscription was disabled."""

    end_date: str
    """The time in ISO 8601 format when the subscription ended."""

    grace_period_id: Optional[str] = UNSET
    """The ID of the grace period."""

    id: str
    """The ID of the subscription."""

    is_latest: bool
    """Whether the subscription is the latest version."""

    payment_method_id: str
    """The ID of the payment method."""

    plans: list[Plan]
    """An array of plans in the subscription."""

    start_date: str
    """The time in ISO 8601 format when the subscription started."""

    status: Status16OrStr
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

    subscription_number: str
    """The number of the subscription."""

    subscription_version: float
    """The version of the subscription."""

    updated_at: str
    """The time in ISO 8601 format when the subscription was updated."""

    vendor: str
    """The vendor of the subscription."""


class SubscriptionDict(TypedDict):
    account_id: str
    auto_renew: bool
    can_renew_now: bool
    created_at: str
    disabled_at: NotRequired[str]
    end_date: str
    grace_period_id: NotRequired[str]
    id: str
    is_latest: bool
    payment_method_id: str
    plans: list[Plan | PlanDict]
    start_date: str
    status: Status16OrStr
    subscription_number: str
    subscription_version: float
    updated_at: str
    vendor: str
