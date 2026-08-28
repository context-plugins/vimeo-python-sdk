from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackViews(SdkBaseModel):
    """Information about showing the view count during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to show the view count during playback."""

    value: bool
    """Whether to show the view count during playback."""


class ShowPlaybackViewsDict(TypedDict):
    is_upgrade: bool
    value: bool
