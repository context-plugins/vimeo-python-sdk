from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowPlaybackGridProfileName(SdkBaseModel):
    """Information about showing the profile name in grid view."""

    is_upgrade: bool
    """Whether an upgrade is required to show the profile name in grid view."""

    value: bool
    """Whether to show the profile name in grid view."""


class ShowPlaybackGridProfileNameDict(TypedDict):
    is_upgrade: bool
    value: bool
