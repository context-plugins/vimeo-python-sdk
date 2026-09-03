from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowGridProfileImage(SdkBaseModel):
    """Information about showing the profile image on each video."""

    is_upgrade: bool
    """Whether an upgrade is required to show the profile image on each video."""

    value: bool
    """Whether to show the profile image on each video."""


class ShowGridProfileImageDict(TypedDict):
    is_upgrade: bool
    value: bool
