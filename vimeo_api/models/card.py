from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Card(SdkBaseModel):
    display_time: float
    """The number of seconds for which the card appears."""

    headline: str
    """The title of the card."""

    id: str
    """The UUID of the card."""

    image_url: str
    """The URL of the thumbnail for the card."""

    teaser: str
    """The description of the card."""

    timecode: float
    """The playback timestamp, given in seconds, when the card appears."""

    url: str
    """The URL of the card."""


class CardDict(TypedDict):
    display_time: float
    headline: str
    id: str
    image_url: str
    teaser: str
    timecode: float
    url: str
