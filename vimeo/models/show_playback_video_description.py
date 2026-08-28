from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackVideoDescription(SdkBaseModel):
    """Information about showing the video description during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to show the video description during playback."""

    value: bool
    """Whether to show the video description during playback."""


class ShowPlaybackVideoDescriptionDict(TypedDict):
    is_upgrade: bool
    value: bool
