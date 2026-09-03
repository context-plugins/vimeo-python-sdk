from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Video4(SdkBaseModel):
    """Video metadata information."""

    codec: str
    """The raw video codec of the source file."""

    display_codec: str
    """A human-readable version of the video codec name, such as ``MP4``, ``WebM``, or ``MOV``, or the raw codec value,
    depending on the codec."""

    fps: float | None
    """The frames per second of the source video."""

    height: float
    """The height of the source video in pixels."""

    projection: str
    """The spatial projection type of the source video."""

    stereo_mode: str
    """The stereo mode of the source video."""

    width: float
    """The width of the source video in pixels."""


class Video4Dict(TypedDict):
    codec: str
    display_codec: str
    fps: float | None
    height: float
    projection: str
    stereo_mode: str
    width: float
