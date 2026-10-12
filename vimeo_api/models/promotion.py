from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .price1 import Price1, Price1Dict
from .price_formatted1 import PriceFormatted1, PriceFormatted1Dict
from .uri1 import Uri1, Uri1Dict


class Promotion(SdkBaseModel):
    """Information about the plan's promotion."""

    code: str
    """The promotion code."""

    discount: float
    """The promotion discount percentage."""

    price: Price1
    """The price map of the promotion."""

    price_formatted: PriceFormatted1
    """The price map of the promotion formatted for the selected locale."""

    uri: Uri1
    """Information about the URIs associated with the promotion."""


class PromotionDict(TypedDict):
    code: str
    discount: float
    price: Price1Dict
    price_formatted: PriceFormatted1Dict
    uri: Uri1Dict
