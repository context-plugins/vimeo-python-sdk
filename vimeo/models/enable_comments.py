from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EnableComments(SdkBaseModel):
    """Information about enabling the comments functionality during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to enable the comments functionality during playback."""

    value: bool
    """Whether to enable the comments functionality during playback."""


class EnableCommentsDict(TypedDict):
    is_upgrade: bool
    value: bool
