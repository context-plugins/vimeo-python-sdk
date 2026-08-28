from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OnDemandPromotionCode(SdkBaseModel):
    code: str
    """The Vimeo promotion code."""

    link: str
    """The link to redeem the promotion code."""

    max_uses: float
    """The total number of times that this code can be used."""

    uses: float
    """The current number of times that this code has been used."""


class OnDemandPromotionCodeDict(TypedDict):
    code: str
    link: str
    max_uses: float
    uses: float
