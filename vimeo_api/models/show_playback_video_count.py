from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackVideoCount(SdkBaseModel):
    """Information about showing the video count during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to show the video count during playback."""

    value: bool
    """Whether to show the video count during playback."""


class ShowPlaybackVideoCountDict(TypedDict):
    is_upgrade: bool
    value: bool
