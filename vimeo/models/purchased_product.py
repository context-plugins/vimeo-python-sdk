from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PurchasedProduct(SdkBaseModel):
    """Information about the purchased product."""

    display_price: float
    """The display price of the purchased product."""

    display_price_formatted: str
    """The display price of the purchased product formatted for the selected locale."""

    is_monthly: bool
    """Whether the purchased product is billed as a monthly subscription."""


class PurchasedProductDict(TypedDict):
    display_price: float
    display_price_formatted: str
    is_monthly: bool
