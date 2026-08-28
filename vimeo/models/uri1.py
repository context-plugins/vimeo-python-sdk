from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Uri1(SdkBaseModel):
    """Information about the URIs associated with the promotion."""

    annual: Optional[str] = UNSET
    """The URI of the annual promotion."""

    monthly: Optional[str] = UNSET
    """The URI of the monthly promotion."""


class Uri1Dict(TypedDict):
    annual: NotRequired[str]
    monthly: NotRequired[str]
