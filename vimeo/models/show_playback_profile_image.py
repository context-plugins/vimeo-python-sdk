from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackProfileImage(SdkBaseModel):
    """Information about showing the profile image during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to show the profile image during playback."""

    value: bool
    """Whether to show the profile image during playback."""


class ShowPlaybackProfileImageDict(TypedDict):
    is_upgrade: bool
    value: bool
