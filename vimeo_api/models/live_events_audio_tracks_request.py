from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LiveEventsAudioTracksRequest(SdkBaseModel):
    audio_tracks: Optional[list[str]] = UNSET
    """A list of language codes for audio tracks."""

    primary_audio_track: Optional[str] = UNSET
    """The language code for the primary audio track."""


class LiveEventsAudioTracksRequestDict(TypedDict):
    audio_tracks: NotRequired[list[str]]
    primary_audio_track: NotRequired[str]
