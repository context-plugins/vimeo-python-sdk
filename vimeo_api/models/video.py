from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_app import ApiApp, ApiAppDict
from .category import Category, CategoryDict
from .context import Context, ContextDict
from .custom_metadatum import CustomMetadatum, CustomMetadatumDict
from .deleted_by import DeletedBy, DeletedByDict
from .editing_session import EditingSession, EditingSessionDict
from .embed_settings import EmbedSettings, EmbedSettingsDict
from .enums.content_rating4 import ContentRating4OrStr
from .enums.content_rating_class import ContentRatingClassOrStr
from .enums.license1 import License1OrStr
from .enums.review_status import ReviewStatusOrStr
from .enums.status4 import Status4OrStr
from .enums.type7 import Type7OrStr
from .explicit_access_summary import ExplicitAccessSummary, ExplicitAccessSummaryDict
from .metadata4 import Metadata4, Metadata4Dict
from .picture import Picture, PictureDict
from .play import Play, PlayDict
from .privacy3 import Privacy3, Privacy3Dict
from .project import Project, ProjectDict
from .review_link import ReviewLink, ReviewLinkDict
from .spatial import Spatial, SpatialDict
from .stats import Stats, StatsDict
from .tag import Tag, TagDict
from .transcode import Transcode, TranscodeDict
from .transcript import Transcript, TranscriptDict
from .upload import Upload, UploadDict
from .uploader import Uploader, UploaderDict
from .user import User, UserDict
from .version_transcode_status import VersionTranscodeStatus, VersionTranscodeStatusDict
from .video_file import VideoFile, VideoFileDict
from .video_page_settings import VideoPageSettings, VideoPageSettingsDict
from .video_versions_size import VideoVersionsSize, VideoVersionsSizeDict
from .vod import Vod, VodDict


class Video(SdkBaseModel):
    allow_multiple_review_links: Optional[bool] = UNSET
    """Whether the video can have multiple review links."""

    allowed_privacies: Optional[list[str]] = UNSET
    """An array of privacy settings supported for this video and the requesting user."""

    app: ApiApp
    """The API application associated with the video owner's token."""

    can_move_to_project: bool
    """Whether the video can be moved to a folder. This data requires a bearer token with the ``private`` scope."""

    categories: list[Category]
    """The categories that the video belongs to."""

    content_rating: ContentRating4OrStr
    """The video's granular content rating.

    Option descriptions:
     * ``advertisement`` - The video contains advertisements.
     * ``drugs`` - The video contains drug or alcohol use.
     * ``language`` - The video contains profanity or sexually suggestive content.
     * ``nudity`` - The video contains nudity.
     * ``safe`` - The video is safe for all audiences.
     * ``unrated`` - The video hasn't been rated.
     * ``violence`` - The video contains violence."""

    content_rating_class: ContentRatingClassOrStr
    """The video's high-level content rating class.

    Option descriptions:
     * ``explicit`` - The video contains one or more explicit content rating types.
     * ``safe`` - The video contains no explicit content rating types.
     * ``unrated`` - The video doesn't belong to a content rating class."""

    context: Context
    """The context of the video's subscription, if the video is part of a subscription."""

    counts_toward_managed_storage: bool
    """Whether this video counts toward the owner's managed (restricted) storage limit — i.e. it is non-public OR
    embeddable. Only rendered for owners that actually have a managed storage cap (repackaged / REPACK_FREE plans);
    omitted otherwise, since the two-pool model does not apply. Clients use this to mark managed-storage videos and to
    offer the "make it public & non-embeddable to free managed storage / unfreeze" affordance."""

    created_time: str
    """The time in ISO 8601 format when the video was created."""

    custom_metadata: Optional[list[CustomMetadatum]] = UNSET
    """The video's custom metadata fields with their settings and current values."""

    custom_url: str | None
    """The custom URL of the video."""

    deleted_by: DeletedBy | None
    """The user who deleted this video. Null if the video was moved to cold storage automatically."""

    description: str | None
    """A brief explanation of the video's content."""

    description_html: str
    """A brief explanation of the video's content, formatted with HTML entities."""

    description_rich: Optional[str] = UNSET
    """A JSON representation of the description."""

    download: Optional[list[VideoFile]] = UNSET
    """The list of downloadable files for the video. This data requires a bearer token with the ``private`` scope."""

    duration: float
    """The video's duration in seconds. A value of ``0`` indicates the duration hasn't been calculated yet."""

    edit_session: Optional[EditingSession] = UNSET
    """Information about the video's Vimeo Create editing session. This data requires a bearer token with the
    ``private`` scope."""

    embed: EmbedSettings
    """Information about embedding the video."""

    explicit_access_summary: Optional[ExplicitAccessSummary] = UNSET
    """The explicit access summary of the video. This data requires a bearer token with the ``private`` scope."""

    files: Optional[list[VideoFile]] = UNSET
    """The list of files for the video. This data requires a bearer token with the ``private`` scope."""

    files_size: VideoVersionsSize
    """The total combined file size for all versions of the video, and the file size type."""

    has_audio: bool
    """Whether the video has audio."""

    has_audio_tracks: bool
    """Whether the video has alternate audio tracks."""

    has_chapters: bool
    """Whether the video has chapters."""

    has_interactive: Optional[bool] = UNSET
    """Whether the video has interactive capability."""

    has_text_tracks: bool
    """Whether the video has text tracks."""

    height: float
    """The video's height in pixels."""

    is_cold_privacy_restricted: bool
    """Whether the video's privacy is being suppressed to private because the owner's current plan no longer supports
    its original privacy setting (for example, a previously unlisted video on a downgraded/free account). The video's
    stored privacy is preserved as the owner's intent and served back automatically if the owner upgrades again.
    Distinct from ``is_cold_storage``, which covers videos frozen for exceeding the plan's storage limit."""

    is_cold_storage: bool
    """Whether the video has been moved to cold storage."""

    is_copyright_restricted: bool
    """Whether the video is privacy restricted due to a copyright infringement. This data requires a bearer token with
    the ``private`` scope."""

    is_free: Optional[bool] = UNSET
    """Whether the video is a free Vimeo Stock video."""

    is_playable: bool
    """Whether the video is playable."""

    is_starred_by_cur_user: bool
    """Whether the current user has starred this video."""

    language: str | None
    """The video's primary language."""

    last_user_action_event_date: OptionalNullable[str] = UNSET
    """The time in ISO 8601 format when the user last modified the video."""

    license: License1OrStr
    """The `Creative Commons <http://creativecommons.org/licenses/>`__ license that the video is given under.

    Option descriptions:
     * `` - No Creative Commons license has been set for the video.
     * ``by`` - The video is given under the Attribution license.
     * ``by-nc`` - The video is given under the Attribution Non-Commercial license.
     * ``by-nc-nd`` - The video is given under the Attribution Non-Commercial No Derivatives license.
     * ``by-nc-sa`` - The video is given under the Attribution Non-Commercial Share Alike license.
     * ``by-nd`` - The video is given under the Attribution No Derivatives license.
     * ``by-sa`` - The video is given under the Attribution Share Alike license.
     * ``cc0`` - The video is given under the Public Domain Dedication license."""

    link: str
    """The link to the video."""

    manage_link: Optional[str] = UNSET
    """The link to the video management page. This data requires a bearer token with the ``private`` scope."""

    metadata: Metadata4
    """The video's metadata."""

    modified_time: str
    """The time in ISO 8601 format when the video metadata was last modified."""

    name: str
    """The video's title."""

    origin_variable_frame_resolution: Optional[bool] = UNSET
    """Whether the video has unified resolution. If the value of this field is ``false``, the video requires
    transcoding."""

    page: Optional[VideoPageSettings] = UNSET
    """Information about the video's page settings. This data requires a bearer token with the ``private`` scope."""

    parent_project: OptionalNullable[Project] = UNSET
    """Information about the project that contains the video."""

    password: Optional[str] = UNSET
    """The privacy-enabled password to watch the video. Only the video's owner and team members with permission can
    access the video's password. This data requires a bearer token with the ``private`` scope."""

    pictures: Picture
    """The video's active picture."""

    play: Optional[Play] = UNSET
    """The ``Play`` representation."""

    player_embed_url: str
    """The video's player embed URL."""

    privacy: Privacy3
    """The video's privacy setting."""

    rating_mod_locked: bool
    """Whether the video's content rating is locked by a moderator."""

    release_time: str
    """The time in ISO 8601 format when the video was released."""

    resource_key: str
    """The resource key string of the video."""

    review_links: Optional[list[ReviewLink]] = UNSET
    """All active review links associated with the video."""

    review_status: Optional[ReviewStatusOrStr] = UNSET
    """The review status of the video.

    Option descriptions:
     * ``approved`` - The video review was approved.
     * ``in_progress`` - The video review is in progress.
     * ``needs_review`` - The video needs to be reviewed."""

    show_review_page: bool
    """Whether to show the button for reviews on single video view recipient pages. This data requires a bearer token
    with the ``private`` scope."""

    show_svv_footer_banner: bool
    """Whether to show the single video view footer banner on recipient pages. This data requires a bearer token with
    the ``private`` scope."""

    show_svv_timecoded_comments: bool
    """Whether to enable timecoded comments on the single video view recipient page. This data requires a bearer token
    with the ``private`` scope."""

    spatial: Optional[Spatial] = UNSET
    """The video's 360 spatial data."""

    stats: Stats
    """A collection of analytics associated with the video."""

    status: Status4OrStr
    """The status code for the availability of the video.

    Option descriptions:
     * ``available`` - The video is available.
     * ``failed`` - There was an error in rendering the video.
     * ``processing`` - Rendering has started and is currently underway for the video.
     * ``quota_exceeded`` - The user's weekly upload quota is exceeded with this video.
     * ``total_cap_exceeded`` - The user's total storage limit is exceeded with this video.
     * ``transcode_starting`` - Transcoding is starting for the video.
     * ``transcoding`` - Transcoding has started and is currently underway for the video.
     * ``transcoding_error`` - There was an error in transcoding the video.
     * ``unavailable`` - The video is unavailable.
     * ``uploading`` - The video is being uploaded.
     * ``uploading_error`` - There was an error in uploading the video."""

    tags: list[Tag]
    """An array of all tags assigned to the video."""

    transcode: Transcode | None
    """The transcode information of the video upload."""

    transcript: Transcript
    """The transcript information of the video. This data requires a bearer token with the ``private`` scope."""

    type_: Type7OrStr = Field(alias="type")
    """The type of the video.

    Option descriptions:
     * ``live`` - The video is or was an event.
     * ``stock`` - The video is a Vimeo Stock video.
     * ``video`` - The video is a standard Vimeo video."""

    upload: Upload | None
    """The video's upload information."""

    uploader: Uploader
    """The video's uploader."""

    uri: str
    """The video's canonical relative URI."""

    user: User
    """The video's owner."""

    uses_drm: bool
    """Whether the video uses digital rights management."""

    version_transcode_status: VersionTranscodeStatus
    """Detailed transcode status information for the current version of the video upload."""

    vod: Vod
    """The video's Vimeo On Demand information."""

    width: float
    """The video's width in pixels."""


class VideoDict(TypedDict):
    allow_multiple_review_links: NotRequired[bool]
    allowed_privacies: NotRequired[list[str]]
    app: ApiApp | ApiAppDict
    can_move_to_project: bool
    categories: list[Category | CategoryDict]
    content_rating: ContentRating4OrStr
    content_rating_class: ContentRatingClassOrStr
    context: Context | ContextDict
    counts_toward_managed_storage: bool
    created_time: str
    custom_metadata: NotRequired[list[CustomMetadatum | CustomMetadatumDict]]
    custom_url: str | None
    deleted_by: DeletedBy | DeletedByDict | None
    description: str | None
    description_html: str
    description_rich: NotRequired[str]
    download: NotRequired[list[VideoFile | VideoFileDict]]
    duration: float
    edit_session: NotRequired[EditingSession | EditingSessionDict]
    embed: EmbedSettings | EmbedSettingsDict
    explicit_access_summary: NotRequired[ExplicitAccessSummary | ExplicitAccessSummaryDict]
    files: NotRequired[list[VideoFile | VideoFileDict]]
    files_size: VideoVersionsSize | VideoVersionsSizeDict
    has_audio: bool
    has_audio_tracks: bool
    has_chapters: bool
    has_interactive: NotRequired[bool]
    has_text_tracks: bool
    height: float
    is_cold_privacy_restricted: bool
    is_cold_storage: bool
    is_copyright_restricted: bool
    is_free: NotRequired[bool]
    is_playable: bool
    is_starred_by_cur_user: bool
    language: str | None
    last_user_action_event_date: NotRequired[str | None]
    license: License1OrStr
    link: str
    manage_link: NotRequired[str]
    metadata: Metadata4 | Metadata4Dict
    modified_time: str
    name: str
    origin_variable_frame_resolution: NotRequired[bool]
    page: NotRequired[VideoPageSettings | VideoPageSettingsDict]
    parent_project: NotRequired[Project | ProjectDict | None]
    password: NotRequired[str]
    pictures: Picture | PictureDict
    play: NotRequired[Play | PlayDict]
    player_embed_url: str
    privacy: Privacy3 | Privacy3Dict
    rating_mod_locked: bool
    release_time: str
    resource_key: str
    review_links: NotRequired[list[ReviewLink | ReviewLinkDict]]
    review_status: NotRequired[ReviewStatusOrStr]
    show_review_page: bool
    show_svv_footer_banner: bool
    show_svv_timecoded_comments: bool
    spatial: NotRequired[Spatial | SpatialDict]
    stats: Stats | StatsDict
    status: Status4OrStr
    tags: list[Tag | TagDict]
    transcode: Transcode | TranscodeDict | None
    transcript: Transcript | TranscriptDict
    type_: Type7OrStr
    upload: Upload | UploadDict | None
    uploader: Uploader | UploaderDict
    uri: str
    user: User | UserDict
    uses_drm: bool
    version_transcode_status: VersionTranscodeStatus | VersionTranscodeStatusDict
    vod: Vod | VodDict
    width: float
