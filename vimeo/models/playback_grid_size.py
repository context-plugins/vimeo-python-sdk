from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PlaybackGridSize(SdkBaseModel):
    """Information about the grid size configuration for playback view."""

    is_upgrade: bool
    """Whether an upgrade is required to configure the playback grid size."""

    value: str
    """The grid size configuration for playback view. Possible values include ``s`` for small, ``m`` for medium, ``l``
    for large, and ``xl`` for extra large."""


class PlaybackGridSizeDict(TypedDict):
    is_upgrade: bool
    value: str
