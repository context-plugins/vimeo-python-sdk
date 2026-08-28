from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .metadata28 import Metadata28, Metadata28Dict


class TrimmedVideo(SdkBaseModel):
    clip_id: float
    """The ID of the video. _This field is deprecated._"""

    created_on: str
    """The time in ISO 8601 format when the trim was created."""

    created_version_id: str
    """The most recent version of the trimmed video. _This field is deprecated._"""

    end: str
    """The end of the trim from the last trim, in seconds."""

    is_clip_finished_transcoding: bool
    """Whether the transcoding jobs for the video file have finished. _This field is deprecated._"""

    metadata: Metadata28
    modified_on: str | None
    """The time in ISO 8601 format when the trim policy was last modified."""

    root_version_id: str
    """The video version that is the source of the trimmed video. _This field is deprecated._"""

    start: str
    """The start of the trim from the last trim, in seconds."""

    uri: str
    """The URI of the player or the trim service. _This field is deprecated._"""

    version_quality: str
    """The quality of the root version video file."""


class TrimmedVideoDict(TypedDict):
    clip_id: float
    created_on: str
    created_version_id: str
    end: str
    is_clip_finished_transcoding: bool
    metadata: Metadata28 | Metadata28Dict
    modified_on: str | None
    root_version_id: str
    start: str
    uri: str
    version_quality: str
