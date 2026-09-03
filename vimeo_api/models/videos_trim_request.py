from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosTrimRequest(SdkBaseModel):
    trim_end: Optional[str] = UNSET
    """The end position in seconds of the trim in the video."""

    trim_start: Optional[str] = UNSET
    """The start position in seconds of the trim in the video."""


class VideosTrimRequestDict(TypedDict):
    trim_end: NotRequired[str]
    trim_start: NotRequired[str]
