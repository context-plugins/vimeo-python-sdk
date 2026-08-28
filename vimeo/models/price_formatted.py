from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PriceFormatted(SdkBaseModel):
    """The price formatted for the selected locale with the associated currency symbol."""

    annual: str
    """The annual price, charged annually."""

    annual_monthly: str
    """The monthly price, charged annually."""

    monthly: Optional[str] = UNSET
    """The monthly price, charged monthly."""


class PriceFormattedDict(TypedDict):
    annual: str
    annual_monthly: str
    monthly: NotRequired[str]
