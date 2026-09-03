from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackUploadedDate(SdkBaseModel):
    """Information about showing the date when the video was uploaded during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to show the date when the video was uploaded during playback."""

    value: bool
    """Whether to show the date when the video was uploaded during playback."""


class ShowPlaybackUploadedDateDict(TypedDict):
    is_upgrade: bool
    value: bool
