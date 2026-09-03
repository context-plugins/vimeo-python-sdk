from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowGridVideoCount(SdkBaseModel):
    """Information about showing the video count above the video list."""

    is_upgrade: bool
    """Whether an upgrade is required to show the video count above the video list."""

    value: bool
    """Whether to show the video count above the video list."""


class ShowGridVideoCountDict(TypedDict):
    is_upgrade: bool
    value: bool
