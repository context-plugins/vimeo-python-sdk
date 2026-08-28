from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AnimatedThumbnail(SdkBaseModel):
    duration: float
    """The duration of the animated thumbnail in seconds."""

    file_format: str
    """The file format of the animated thumbnail."""

    file_size: float
    """The file size of the animated thumbnail in bytes."""

    height: float
    """The height of the animated thumbnail in pixels."""

    is_downloadable: bool
    """Whether the animated thumbnail can be downloaded."""

    link: str
    """The URL of the animated thumbnail file."""

    link_with_play_button: str
    """The URL of the animated thumbnail file with a play button overlay."""

    profile_id: str
    """The profile ID of the animated thumbnail."""

    start_time: float
    """The time in the video, in seconds, corresponding to the start of the animation."""

    uuid: str
    """The ID of the animated thumbnail."""

    width: float
    """The width of the animated thumbnail in pixels."""


class AnimatedThumbnailDict(TypedDict):
    duration: float
    file_format: str
    file_size: float
    height: float
    is_downloadable: bool
    link: str
    link_with_play_button: str
    profile_id: str
    start_time: float
    uuid: str
    width: float
