from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reason5 import Reason5OrStr


class Highlights(SdkBaseModel):
    """Information about where and how to create a highlight for the video."""

    disabled: Optional[bool] = UNSET
    """Whether the interaction is disabled for the video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    reason: Optional[Reason5OrStr] = UNSET
    """The reason why the interaction is disabled.

    Option descriptions:
     * ``owner_disabled_feature_group`` - The owner has disabled the feature group.
     * ``transcript_status_does_not_exist`` - The transcript doesn't exist.
     * ``transcript_status_failed`` - The transcript job failed.
     * ``transcript_status_in_progress`` - The transcript job is in progress.
     * ``transcript_status_no_speech`` - There's no speech detected for the transcript.
     * ``transcript_status_not_started`` - The transcript job hasn't started.
     * ``transcript_status_unknown`` - The transcript job status is unknown.
     * ``video_not_ready`` - The video isn't ready.
     * ``video_resolution_too_low`` - The video resolution is below the 360p minimum requirement.
     * ``video_too_short`` - The video is too short.
     * ``video_transcript_too_short`` - The video transcript is too short."""

    uri: str
    """The API URI that resolves to the connection data."""


class HighlightsDict(TypedDict):
    disabled: NotRequired[bool]
    options: list[str]
    reason: NotRequired[Reason5OrStr]
    uri: str
