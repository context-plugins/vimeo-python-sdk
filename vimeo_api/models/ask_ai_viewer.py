from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.reason4 import Reason4OrStr


class AskAiViewer(SdkBaseModel):
    """Information about where and how to submit questions by viewers to the AI service for this video."""

    disabled: bool
    """Whether Ask AI is disabled."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    reason: Reason4OrStr | None
    """The reason why Ask AI is disabled.

    Option descriptions:
     * ``transcript_status_does_not_exist`` - The transcript doesn't exist.
     * ``transcript_status_exceeds_maximum_duration`` - The transcript duration is too long.
     * ``transcript_status_failed`` - The transcript job failed.
     * ``transcript_status_in_progress`` - The transcript job is in progress.
     * ``transcript_status_language_not_supported`` - The transcript's language isn't supported.
     * ``transcript_status_no_speech`` - There's no speech detected for the transcript.
     * ``transcript_status_not_started`` - The transcript job hasn't started.
     * ``transcript_status_unknown`` - The transcript job status is unknown.
     * ``video_not_ready`` - The video isn't ready.
     * ``video_too_short`` - The video is too short.
     * ``video_transcript_too_short`` - The video transcript is too short."""

    uri: str
    """The API URI that resolves to the connection data."""


class AskAiViewerDict(TypedDict):
    disabled: bool
    options: list[str]
    reason: Reason4OrStr | None
    uri: str
