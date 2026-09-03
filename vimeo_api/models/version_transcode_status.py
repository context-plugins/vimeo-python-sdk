from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class VersionTranscodeStatus(SdkBaseModel):
    is_complete: bool
    """Whether the video has finished transcoding."""

    is_fully_playable: bool
    """Whether the video is playable in all resolutions, up to either the source quality or 4K, whichever is lower, at
    standard definition."""

    is_playable: bool
    """Whether the video is playable."""


class VersionTranscodeStatusDict(TypedDict):
    is_complete: bool
    is_fully_playable: bool
    is_playable: bool
