from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .items1 import Items1, Items1Dict
from .money import Money, MoneyDict


class Plan(SdkBaseModel):
    amount: Optional[Money] = UNSET
    """The amount of the plan."""

    billing_plan_id: Optional[str] = UNSET
    """The ID of the billing plan."""

    billing_plan_product_id: Optional[str] = UNSET
    """The ID of the billing plan product."""

    billing_plan_type: Optional[str] = UNSET
    """The type of the billing plan."""

    created_at: str
    """The time in 8601 format when the plan was created."""

    id: str
    """The ID of the plan."""

    items: list[Items1]
    """An array of items in the plan."""

    metadata: Optional[Any] = UNSET
    """The metadata of the plan."""

    plan_id: str
    """The ID of the plan."""

    product_id: str
    """The ID of the product."""

    promo_code: Optional[str] = UNSET
    """The promotional code."""

    promo_code_id: Optional[str] = UNSET
    """The ID of the promotional code."""

    quantity: Optional[float] = UNSET
    """The quantity of the plan."""

    subscription_plan_id: str
    """The ID of the subscription plan."""

    subscription_plan_number: str
    """The number of the subscription plan."""

    subscription_plan_type: str
    """The type of the subscription plan."""

    synced_at: str
    """The time in 8601 format when the plan was synced."""

    updated_at: str
    """The time in 8601 format when the plan was updated."""


class PlanDict(TypedDict):
    amount: NotRequired[Money | MoneyDict]
    billing_plan_id: NotRequired[str]
    billing_plan_product_id: NotRequired[str]
    billing_plan_type: NotRequired[str]
    created_at: str
    id: str
    items: list[Items1 | Items1Dict]
    metadata: NotRequired[Any]
    plan_id: str
    product_id: str
    promo_code: NotRequired[str]
    promo_code_id: NotRequired[str]
    quantity: NotRequired[float]
    subscription_plan_id: str
    subscription_plan_number: str
    subscription_plan_type: str
    synced_at: str
    updated_at: str
