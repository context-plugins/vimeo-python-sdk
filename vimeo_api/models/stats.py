from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Stats(SdkBaseModel):
    """A collection of analytics associated with the video."""

    plays: float | None
    """The current total number of times that the video has been played."""


class StatsDict(TypedDict):
    plays: float | None
