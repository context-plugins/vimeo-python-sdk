from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Audio(SdkBaseModel):
    """Audio metadata information."""

    channels: float
    """The number of audio channels in the source file."""

    codec: str
    """The raw audio codec of the source file."""

    display_codec: str
    """A human-readable version of the audio codec name, such as ``AAC``, ``MP3``, or ``Opus``, or the raw codec value,
    depending on the codec."""


class AudioDict(TypedDict):
    channels: float
    codec: str
    display_codec: str
