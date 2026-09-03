from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PriceFormatted1(SdkBaseModel):
    """The price map of the promotion formatted for the selected locale."""

    annual: Optional[str] = UNSET
    """The promotional annual price, charged annually."""

    annual_monthly: Optional[str] = UNSET
    """The promotional monthly price, charged annually."""

    monthly: Optional[str] = UNSET
    """The promotional monthly price, charged monthly."""


class PriceFormatted1Dict(TypedDict):
    annual: NotRequired[str]
    annual_monthly: NotRequired[str]
    monthly: NotRequired[str]
