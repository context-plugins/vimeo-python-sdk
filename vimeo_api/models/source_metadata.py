from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .audio import Audio, AudioDict
from .video4 import Video4, Video4Dict


class SourceMetadata(SdkBaseModel):
    """Metadata about the source file."""

    audio: Audio | None
    """Audio metadata information."""

    display_filetype: str | None
    """A human-readable version of the source video MIME type, such as ``MP4``, ``WebM``, or ``MOV``, or the raw MIME
    type, depending on the MIME type."""

    filetype: str | None
    """The MIME type of the source video."""

    video: Video4 | None
    """Video metadata information."""


class SourceMetadataDict(TypedDict):
    audio: AudioDict | None
    display_filetype: str | None
    filetype: str | None
    video: Video4Dict | None
