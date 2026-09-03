from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .api_app import ApiApp, ApiAppDict
from .audio_track_quota import AudioTrackQuota, AudioTrackQuotaDict
from .edit_session import EditSession, EditSessionDict
from .enums.version_transcode_status1 import VersionTranscodeStatus1OrStr
from .enums.version_type import VersionTypeOrStr
from .metadata29 import Metadata29, Metadata29Dict
from .picture import Picture, PictureDict
from .play import Play, PlayDict
from .source_metadata import SourceMetadata, SourceMetadataDict
from .transcode2 import Transcode2, Transcode2Dict
from .upload1 import Upload1, Upload1Dict
from .user import User, UserDict


class VideoVersion(SdkBaseModel):
    active: bool
    """Whether the video version is currently active."""

    app: ApiApp
    """The API app associated with the video version."""

    audio_track_quota: AudioTrackQuota
    """The quota parameters for the audio tracks available for this version."""

    can_restore_create: bool
    """Whether the version can be restored."""

    create_storyboard_id: Optional[str] = UNSET
    """The storyboard ID of the video version."""

    created_time: str
    """The time in ISO 8601 format when the video version was created."""

    description: Optional[str] = UNSET
    """A description of the video version. This description can make use of the full unicode character set. This field
    appears in the response only when a corresponding value is present."""

    download_config: Any
    """The download configuration associated with the version."""

    duration: float | None
    """The duration in seconds of the video version."""

    edit_session: EditSession
    """Information about the video's Vimeo Create editing session. This data requires a bearer token with the
    ``private`` scope."""

    filename: str
    """The file name of the video version."""

    filesize: float | None
    """The size in byes of the video version file."""

    has_interactive: bool
    """Whether the video has interactive capability."""

    height: float | None
    """The height of the version's video."""

    is_deleted: bool
    """Whether the video version has been deleted."""

    is_playable: Optional[bool] = UNSET
    """Whether the video version is playable."""

    metadata: Metadata29
    """The video version's metadata."""

    modified_time: str
    """The time in ISO 8601 format when the video version was last modified."""

    origin_variable_frame_resolution: Optional[bool] = UNSET
    """Whether the video has unified resolution. If the value of this field is ``false``, the video requires
    transcoding."""

    pictures: Picture | None
    """The thumbnail for the video version."""

    play: Optional[Play] = UNSET
    """The ``Play`` representation."""

    player_embed_url: str
    """The embed URL for the video's player. This data requires a bearer token with the ``private`` scope."""

    sequence_number: float | None
    """The sequence number of the video version."""

    source_metadata: SourceMetadata | None
    """Metadata about the source file."""

    transcode: Transcode2 | None
    """The version's transcode information."""

    upload: Upload1 | None
    """The version's upload information."""

    upload_date: str | None
    """The time in ISO 8601 format when the video version was uploaded."""

    uri: str
    """The version's canonical relative URI."""

    user: User | None
    """The owner of the video version."""

    version_transcode_status: Optional[VersionTranscodeStatus1OrStr] = UNSET
    """The transcode status code of the video version.

    Option descriptions:
     * ``complete`` - Transcoding is complete. The video version is available.
     * ``error`` - There was a transcoding error. The video version isn't available.
     * ``in_progress`` - Transcoding is in progress. The video version isn't available yet."""

    version_type: VersionTypeOrStr
    """The type of the version.

    Option descriptions:
     * ``regular`` - The version was generated through a file upload.
     * ``screen-recording`` - The version was generated through Vimeo Record.
     * ``vimeo-create`` - The version was generated through Vimeo Create."""

    width: float | None
    """The width of the version's video."""


class VideoVersionDict(TypedDict):
    active: bool
    app: ApiApp | ApiAppDict
    audio_track_quota: AudioTrackQuota | AudioTrackQuotaDict
    can_restore_create: bool
    create_storyboard_id: NotRequired[str]
    created_time: str
    description: NotRequired[str]
    download_config: Any
    duration: float | None
    edit_session: EditSession | EditSessionDict
    filename: str
    filesize: float | None
    has_interactive: bool
    height: float | None
    is_deleted: bool
    is_playable: NotRequired[bool]
    metadata: Metadata29 | Metadata29Dict
    modified_time: str
    origin_variable_frame_resolution: NotRequired[bool]
    pictures: Picture | PictureDict | None
    play: NotRequired[Play | PlayDict]
    player_embed_url: str
    sequence_number: float | None
    source_metadata: SourceMetadata | SourceMetadataDict | None
    transcode: Transcode2 | Transcode2Dict | None
    upload: Upload1 | Upload1Dict | None
    upload_date: str | None
    uri: str
    user: User | UserDict | None
    version_transcode_status: NotRequired[VersionTranscodeStatus1OrStr]
    version_type: VersionTypeOrStr
    width: float | None
