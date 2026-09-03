from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackGridVideoTitle(SdkBaseModel):
    """Information about showing the video title in grid view."""

    is_upgrade: bool
    """Whether an upgrade is required to show the video title in grid view."""

    value: bool
    """Whether to show the video title in grid view."""


class ShowPlaybackGridVideoTitleDict(TypedDict):
    is_upgrade: bool
    value: bool
