from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price1(SdkBaseModel):
    """The price map of the promotion."""

    annual: Optional[float] = UNSET
    """The promotional annual price, charged annually."""

    annual_monthly: Optional[float] = UNSET
    """The promotional monthly price, charged annually."""

    monthly: Optional[float] = UNSET
    """The promotional monthly price, charged monthly."""


class Price1Dict(TypedDict):
    annual: NotRequired[float]
    annual_monthly: NotRequired[float]
    monthly: NotRequired[float]
