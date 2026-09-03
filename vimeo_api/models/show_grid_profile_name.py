from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowGridProfileName(SdkBaseModel):
    """Information about showing the profile name on each video."""

    is_upgrade: bool
    """Whether an upgrade is required to show the profile name on each video."""

    value: bool
    """Whether to show the profile name on each video."""


class ShowGridProfileNameDict(TypedDict):
    is_upgrade: bool
    value: bool
