from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price(SdkBaseModel):
    """Information about the prices associated with the plan."""

    annual: float
    """The annual price, charged annually."""

    annual_monthly: float
    """The monthly price, charged annually."""

    monthly: Optional[float] = UNSET
    """The monthly price, charged monthly."""


class PriceDict(TypedDict):
    annual: float
    annual_monthly: float
    monthly: NotRequired[float]
