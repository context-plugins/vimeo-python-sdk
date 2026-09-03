from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Card2(SdkBaseModel):
    display_time: Optional[float] = UNSET
    """The number of seconds for which the card appears."""

    headline: Optional[str] = UNSET
    """The title of the card."""

    id: Optional[str] = UNSET
    """The UUID of the card."""

    image_url: Optional[str] = UNSET
    """The URL of the thumbnail for the card."""

    teaser: Optional[str] = UNSET
    """The description of the card."""

    timecode: Optional[float] = UNSET
    """The playback timestamp, given in seconds, when the card appears."""

    url: Optional[str] = UNSET
    """The URL of the card."""


class Card2Dict(TypedDict):
    display_time: NotRequired[float]
    headline: NotRequired[str]
    id: NotRequired[str]
    image_url: NotRequired[str]
    teaser: NotRequired[str]
    timecode: NotRequired[float]
    url: NotRequired[str]
