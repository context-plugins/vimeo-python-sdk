from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowBanner(SdkBaseModel):
    """Information about showing the banner on the showcase page."""

    is_upgrade: bool
    """Whether an upgrade is required to show the banner on the showcase page."""

    value: bool
    """Whether to show the banner on the showcase page."""


class ShowBannerDict(TypedDict):
    is_upgrade: bool
    value: bool
