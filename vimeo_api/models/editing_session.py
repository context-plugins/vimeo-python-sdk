from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status2 import Status2OrStr


class EditingSession(SdkBaseModel):
    has_watermark: bool
    """Whether the video has a watermark."""

    is_edited_by_tve: bool
    """Whether the video has been edited by Transcript Video Editing."""

    is_max_resolution: bool
    """Whether the current version of the video is at the maximum resolution."""

    is_music_licensed: bool
    """Whether the video has licensed music."""

    is_rated: bool
    """Whether the video has been rated."""

    min_tier_for_movie: str
    """The minimum required Vimeo membership for the user to be able to share the video."""

    result_video_hash: str
    """The result video hash for the created video."""

    status: Status2OrStr
    """The status of the video.

    Option descriptions:
     * ``done`` - The video is finished processing.
     * ``failed`` - Video processing has failed.
     * ``processing`` - The video is still being processed."""

    upload_attempt_id_version_uri: Optional[str] = UNSET
    """The version's canonical relative URI."""

    version_uri: Optional[str] = UNSET
    """The version's canonical relative URI."""

    vsid: float
    """The ID of the video's editing session."""


class EditingSessionDict(TypedDict):
    has_watermark: bool
    is_edited_by_tve: bool
    is_max_resolution: bool
    is_music_licensed: bool
    is_rated: bool
    min_tier_for_movie: str
    result_video_hash: str
    status: Status2OrStr
    upload_attempt_id_version_uri: NotRequired[str]
    version_uri: NotRequired[str]
    vsid: float
