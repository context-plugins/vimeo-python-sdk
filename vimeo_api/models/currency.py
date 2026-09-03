from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Currency(SdkBaseModel):
    """Information about the currency in which the price of the plan is expressed."""

    currency_code: str
    """The ISO code of the associated currency."""

    symbol: str
    """The symbol of the associated currency."""


class CurrencyDict(TypedDict):
    currency_code: str
    symbol: str
