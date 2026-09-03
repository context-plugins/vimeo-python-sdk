from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Discount(SdkBaseModel):
    """Information about the plan discount."""

    annual: float
    """The annual discount."""


class DiscountDict(TypedDict):
    annual: float
