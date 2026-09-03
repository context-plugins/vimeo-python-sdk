from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Vod(SdkBaseModel):
    """The video's Vimeo On Demand information."""

    id: Optional[float] = UNSET
    """The video's Vimeo On Demand ID."""

    link: str
    """The video's Vimeo On Demand link."""


class VodDict(TypedDict):
    id: NotRequired[float]
    link: str
