from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status6 import Status6OrStr


class Transcript(SdkBaseModel):
    """The transcript information of the video. This data requires a bearer token with the ``private`` scope."""

    language: str | None
    """The video transcript's language. This data requires a bearer token with the ``private`` scope."""

    status: Optional[Status6OrStr] = UNSET
    """The video transcript's availability status. This data requires a bearer token with the ``private`` scope.

    Option descriptions:
     * ``blocked`` - The transcription is blocked.
     * ``completed`` - Transcription is completed. The transcript is available.
     * ``exceeds_maximum_duration`` - The audio track is too long to be transcribed.
     * ``failed`` - There was a transcription error. The transcript isn't available.
     * ``in_progress`` - Transcription is currently underway. The transcript isn't available yet.
     * ``language_not_supported`` - We currently don't support transcribing audio for this video's language.
     * ``no_speech`` - Transcription was completed, but there were no words in the audio to transcribe.
     * ``not_started`` - The transcript job hasn't started.
     * ``unknown`` - There isn't a record of this video's transcription job."""


class TranscriptDict(TypedDict):
    language: str | None
    status: NotRequired[Status6OrStr]
