from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackProfileName(SdkBaseModel):
    """Information about showing the profile name during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to show the profile name during playback."""

    value: bool
    """Whether to show the profile name during playback."""


class ShowPlaybackProfileNameDict(TypedDict):
    is_upgrade: bool
    value: bool
