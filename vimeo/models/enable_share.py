from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EnableShare(SdkBaseModel):
    """Information about enabling the share functionality during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to enable the share functionality during playback."""

    value: bool
    """Whether to enable the share functionality during playback."""


class EnableShareDict(TypedDict):
    is_upgrade: bool
    value: bool
