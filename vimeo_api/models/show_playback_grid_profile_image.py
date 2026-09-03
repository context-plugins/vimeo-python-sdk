from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackGridProfileImage(SdkBaseModel):
    """Information about showing the profile image in grid view."""

    is_upgrade: bool
    """Whether an upgrade is required to show the profile image in grid view."""

    value: bool
    """Whether to show the profile image in grid view."""


class ShowPlaybackGridProfileImageDict(TypedDict):
    is_upgrade: bool
    value: bool
