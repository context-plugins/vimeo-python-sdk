from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowBannerTitle(SdkBaseModel):
    """Information about showing the showcase title."""

    is_upgrade: bool
    """Whether an upgrade is required to show the showcase title."""

    value: bool
    """Whether to show the showcase title."""


class ShowBannerTitleDict(TypedDict):
    is_upgrade: bool
    value: bool
