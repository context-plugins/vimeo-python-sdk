from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Subscription1(SdkBaseModel):
    """Information about subscribing to the On Demand page, if subscription is enabled."""

    active: bool
    """Whether the On Demand product is active."""

    link: str | None
    """The link to the On Demand product."""

    period: Optional[str] = UNSET
    """The On Demand product's rental period."""

    price: Any
    """The accepted currencies and respective pricing for the On Demand product."""


class Subscription1Dict(TypedDict):
    active: bool
    link: str | None
    period: NotRequired[str]
    price: Any
