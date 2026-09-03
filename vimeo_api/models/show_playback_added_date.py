from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackAddedDate(SdkBaseModel):
    """Information about showing the date when the video was added during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to show the date when the video was added during playback."""

    value: bool
    """Whether to show the date when the video was added during playback."""


class ShowPlaybackAddedDateDict(TypedDict):
    is_upgrade: bool
    value: bool
