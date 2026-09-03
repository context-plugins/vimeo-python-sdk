from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackGridVideoCard(SdkBaseModel):
    """Information about showing the video card in grid view."""

    is_upgrade: bool
    """Whether an upgrade is required to show the video card in grid view."""

    value: bool
    """Whether to show the video card in grid view."""


class ShowPlaybackGridVideoCardDict(TypedDict):
    is_upgrade: bool
    value: bool
