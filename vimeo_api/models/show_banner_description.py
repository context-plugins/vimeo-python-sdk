from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowBannerDescription(SdkBaseModel):
    """Information about showing the showcase description."""

    is_upgrade: bool
    """Whether an upgrade is required to show the showcase description."""

    value: bool
    """Whether to show the showcase description."""


class ShowBannerDescriptionDict(TypedDict):
    is_upgrade: bool
    value: bool
