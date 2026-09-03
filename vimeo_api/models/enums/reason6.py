from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Reason6(str, Enum):
    """The reason why the summary method is disabled.

    Option descriptions:
     * ``owner_disabled_feature_group`` - The owner has disabled the feature group.
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

    OWNER_DISABLED_FEATURE_GROUP = "owner_disabled_feature_group"
    TRANSCRIPT_STATUS_DOES_NOT_EXIST = "transcript_status_does_not_exist"
    TRANSCRIPT_STATUS_EXCEEDS_MAXIMUM_DURATION = "transcript_status_exceeds_maximum_duration"
    TRANSCRIPT_STATUS_FAILED = "transcript_status_failed"
    TRANSCRIPT_STATUS_IN_PROGRESS = "transcript_status_in_progress"
    TRANSCRIPT_STATUS_LANGUAGE_NOT_SUPPORTED = "transcript_status_language_not_supported"
    TRANSCRIPT_STATUS_NO_SPEECH = "transcript_status_no_speech"
    TRANSCRIPT_STATUS_NOT_STARTED = "transcript_status_not_started"
    TRANSCRIPT_STATUS_UNKNOWN = "transcript_status_unknown"
    VIDEO_NOT_READY = "video_not_ready"
    VIDEO_TOO_SHORT = "video_too_short"
    VIDEO_TRANSCRIPT_TOO_SHORT = "video_transcript_too_short"

    __str__ = str.__str__


Reason6OrStr: TypeAlias = Annotated[Reason6 | str, open_enum_validator(Reason6)]
