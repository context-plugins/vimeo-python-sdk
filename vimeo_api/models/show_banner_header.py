from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowBannerHeader(SdkBaseModel):
    """Information about showing the showcase header."""

    is_upgrade: bool
    """Whether an upgrade is required to show the showcase header."""

    value: bool
    """Whether to show the showcase header."""


class ShowBannerHeaderDict(TypedDict):
    is_upgrade: bool
    value: bool
