from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EnableLike(SdkBaseModel):
    """Information about enabling the like functionality during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to enable the like functionality during playback."""

    value: bool
    """Whether to enable the like functionality during playback."""


class EnableLikeDict(TypedDict):
    is_upgrade: bool
    value: bool
