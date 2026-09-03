from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EventAudioTracks(SdkBaseModel):
    audio_tracks: list[str]
    """A list of language codes for audio tracks."""

    primary_audio_track: str
    """The language code for the primary audio track."""


class EventAudioTracksDict(TypedDict):
    audio_tracks: list[str]
    primary_audio_track: str
