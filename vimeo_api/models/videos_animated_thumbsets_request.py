from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosAnimatedThumbsetsRequest(SdkBaseModel):
    duration: float
    """The duration of the animation in seconds. The maximum value is 6."""

    start_time: Optional[float] = UNSET
    """The time in seconds corresponding to the start of the animation in the video. The default value is 0."""


class VideosAnimatedThumbsetsRequestDict(TypedDict):
    duration: float
    start_time: NotRequired[float]
