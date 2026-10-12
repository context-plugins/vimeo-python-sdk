from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .picture import Picture, PictureDict


class Recording(SdkBaseModel):
    duration: float | None
    """The duration of the recording, in seconds."""

    link: str
    """The URL to watch the recording."""

    pictures: Picture
    """The recording's thumbnail."""

    streamed_on: str | None
    """When the recording was streamed."""

    title: str | None
    """The title of the recording. Falls back to the event title when the clip has no explicit name."""

    uri: str
    """The canonical URI of the recording."""


class RecordingDict(TypedDict):
    duration: float | None
    link: str
    pictures: PictureDict
    streamed_on: str | None
    title: str | None
    uri: str
