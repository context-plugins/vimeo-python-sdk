from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status6(str, Enum):
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

    BLOCKED = "blocked"
    COMPLETED = "completed"
    EXCEEDS_MAXIMUM_DURATION = "exceeds_maximum_duration"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    LANGUAGE_NOT_SUPPORTED = "language_not_supported"
    NO_SPEECH = "no_speech"
    NOT_STARTED = "not_started"
    UNKNOWN = "unknown"

    __str__ = str.__str__


Status6OrStr: TypeAlias = Annotated[Status6 | str, open_enum_validator(Status6)]
