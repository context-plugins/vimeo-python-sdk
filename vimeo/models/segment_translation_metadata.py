from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SegmentTranslationMetadata(SdkBaseModel):
    audio_out_of_sync: Optional[bool] = UNSET
    """Whether the audio of the translation's segment is out of sync."""

    audio_track_id: Optional[str] = UNSET
    """The ID of the translation's audio track."""

    dominant_language: Optional[str] = UNSET
    """The translation language in ISO 639-1 format."""

    dubbing_id: Optional[str] = UNSET
    """The vendor ID of the translation's dubbing."""

    dubbing_segment_id: Optional[str] = UNSET
    """The vendor ID of the translation's segment."""

    translation_out_of_sync: Optional[bool] = UNSET
    """Whether the translation's segment is out of sync."""


class SegmentTranslationMetadataDict(TypedDict):
    audio_out_of_sync: NotRequired[bool]
    audio_track_id: NotRequired[str]
    dominant_language: NotRequired[str]
    dubbing_id: NotRequired[str]
    dubbing_segment_id: NotRequired[str]
    translation_out_of_sync: NotRequired[bool]
