from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackVideoTitle(SdkBaseModel):
    """Information about showing the video title during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to show the video title during playback."""

    value: bool
    """Whether to show the video title during playback."""


class ShowPlaybackVideoTitleDict(TypedDict):
    is_upgrade: bool
    value: bool
