from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosCreditsRequest1(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the credited person."""

    role: Optional[str] = UNSET
    """The role of the credited person."""


class VideosCreditsRequest1Dict(TypedDict):
    name: NotRequired[str]
    role: NotRequired[str]
