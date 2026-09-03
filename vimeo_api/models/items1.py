from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Items1(SdkBaseModel):
    amount: list[Any]
    """The amount of the item."""

    created_at: str
    """The time in 8601 format when the item was created."""

    end_date: Optional[str] = UNSET
    """The time in 8601 format when the item ended."""

    id: str
    """The ID of the item."""

    metadata: Optional[Any] = UNSET
    """The metadata of the item."""

    price_id: str
    """The ID of the price."""

    quantity: float
    """The quantity of the item."""

    start_date: Optional[str] = UNSET
    """The time in 8601 format when the item started."""

    subscription_item_id: str
    """The ID of the subscription item."""

    subscription_item_number: str
    """The number of the subscription item."""

    subscription_plan_id: str
    """The ID of the subscription plan."""

    synced_at: str
    """The time in 8601 format when the item was synced."""

    updated_at: str
    """The time in 8601 format when the item was updated."""


class Items1Dict(TypedDict):
    amount: list[Any]
    created_at: str
    end_date: NotRequired[str]
    id: str
    metadata: NotRequired[Any]
    price_id: str
    quantity: float
    start_date: NotRequired[str]
    subscription_item_id: str
    subscription_item_number: str
    subscription_plan_id: str
    synced_at: str
    updated_at: str
