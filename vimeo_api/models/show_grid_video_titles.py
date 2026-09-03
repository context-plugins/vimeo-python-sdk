from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowGridVideoTitles(SdkBaseModel):
    """Information about showing the video titles below thumbnails."""

    is_upgrade: bool
    """Whether an upgrade is required to show the video titles below thumbnails."""

    value: bool
    """Whether to show the video titles below thumbnails."""


class ShowGridVideoTitlesDict(TypedDict):
    is_upgrade: bool
    value: bool
