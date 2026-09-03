from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Money(SdkBaseModel):
    amount: float
    """The amount expressed as a numeral without currency formatting."""

    currency: str
    """The currency in which the amount is expressed."""

    formatted: str
    """The amount expressed as a numeral with currency formatting."""

    unit: float
    """The amount expressed as a numeral in the lowest denomination. For example, 12 USD is expressed as 1200."""


class MoneyDict(TypedDict):
    amount: float
    currency: str
    formatted: str
    unit: float
