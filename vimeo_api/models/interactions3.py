from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .album4 import Album4, Album4Dict
from .ask_ai import AskAi, AskAiDict
from .ask_ai_manager import AskAiManager, AskAiManagerDict
from .ask_ai_viewer import AskAiViewer, AskAiViewerDict
from .buy import Buy, BuyDict
from .can_request_team_role_upgrade import CanRequestTeamRoleUpgrade, CanRequestTeamRoleUpgradeDict
from .can_update_privacy_to_public import CanUpdatePrivacyToPublic, CanUpdatePrivacyToPublicDict
from .channel1 import Channel1, Channel1Dict
from .create_editor import CreateEditor, CreateEditorDict
from .delete import Delete, DeleteDict
from .edit import Edit, EditDict
from .edit_privacy import EditPrivacy, EditPrivacyDict
from .has_restricted_privacy_options import HasRestrictedPrivacyOptions, HasRestrictedPrivacyOptionsDict
from .highlights import Highlights, HighlightsDict
from .invite import Invite, InviteDict
from .legal_hold import LegalHold, LegalHoldDict
from .like import Like, LikeDict
from .rent import Rent, RentDict
from .report1 import Report1, Report1Dict
from .set_content_rating import SetContentRating, SetContentRatingDict
from .subscribe import Subscribe, SubscribeDict
from .summary import Summary, SummaryDict
from .text_translations import TextTranslations, TextTranslationsDict
from .transcript_video_editor import TranscriptVideoEditor, TranscriptVideoEditorDict
from .translations import Translations, TranslationsDict
from .trim import Trim, TrimDict
from .validate import Validate, ValidateDict
from .view_privacy import ViewPrivacy, ViewPrivacyDict
from .view_team_members import ViewTeamMembers, ViewTeamMembersDict
from .watched import Watched, WatchedDict
from .watchlater1 import Watchlater1, Watchlater1Dict


class Interactions3(SdkBaseModel):
    """A list of resource URIs related to the video."""

    album: Album4 | None
    """Information about adding or removing a video from the showcase. This information is included only when the video
    is referenced by the URI of a showcase that's moderated by the user."""

    ask_ai: AskAi
    """Information about where and how to submit questions to the AI service for this video."""

    ask_ai_manager: AskAiManager
    """Information about where and how to submit questions by managers to the AI service for this video."""

    ask_ai_viewer: AskAiViewer
    """Information about where and how to submit questions by viewers to the AI service for this video."""

    buy: Buy | None
    """The Buy interaction for the On Demand video."""

    can_comment: Optional[bool] = UNSET
    """Whether the current user can comment on the video on the video management page."""

    can_react_to_collab_comments: bool
    """Whether the current user can add reactions to collaborator comments."""

    can_request_team_role_upgrade: CanRequestTeamRoleUpgrade
    """Information about whether the user can request a team upgrade from the Viewer role."""

    can_update_privacy_to_public: CanUpdatePrivacyToPublic
    """Whether a user can update the video privacy to public."""

    channel: Channel1
    """Information about removing a video from the channel. This information is included only when the video is
    referenced by the URI of a channel that's moderated by the user."""

    create_editor: CreateEditor
    """Information about where and how to edit a video using the Vimeo Create editor."""

    delete: Delete
    """Information about where and how to delete a video."""

    edit: Edit
    """Information about where and how to edit a video."""

    edit_privacy: EditPrivacy
    """Information about editing the privacy of the video."""

    flag_clip: Optional[bool] = UNSET
    """Whether the current user can report the video."""

    has_restricted_privacy_options: HasRestrictedPrivacyOptions
    """Information about whether the video has restricted privacy options."""

    highlights: Highlights
    """Information about where and how to create a highlight for the video."""

    interact: Optional[bool] = UNSET
    """Whether the user can interact with the video."""

    invite: Invite
    """Information about where and how to get a list of team members or groups who were explicitly invited to a video,
    and where and how to invite a team member to a video."""

    legal_hold: LegalHold
    """The associated legal hold object."""

    like: Like
    """Information about whether the user has liked this video."""

    lms_export: Optional[Any] = UNSET
    """Information about whether the video owner has LMS export enabled."""

    rent: Rent | None
    """The Rent interaction for the On Demand video."""

    report: Report1
    """Information about where and how to report a video."""

    set_content_rating: SetContentRating
    """Information about setting a content rating for the video."""

    subscribe: OptionalNullable[Subscribe] = UNSET
    """Subscription information for an On Demand video."""

    summary: Summary
    """Information about whether the current user can create or get a summary for the video."""

    text_translations: TextTranslations
    """Information about where and how to create a text translation for the video."""

    transcript_video_editor: TranscriptVideoEditor
    """Information about where and how to edit a video using the Transcription-based Video Editor editor."""

    translations: Translations
    """Information about where and how to create a translation for the video."""

    trim: Trim
    """Information about where and how to trim the video."""

    validate_value: Validate = Field(alias="validate")
    """Information about where and how to validate a video field."""

    view_privacy: ViewPrivacy
    """Information about whether a user has permissions to view the privacy of the video."""

    view_team_members: ViewTeamMembers
    """Information about whether a user can view the team members associated with a video."""

    watched: Watched
    """Information about removing this video from the user's list of watched videos."""

    watchlater: Watchlater1
    """Information about whether this video appears on the user's Watch Later list."""


class Interactions3Dict(TypedDict):
    album: Album4Dict | None
    ask_ai: AskAiDict
    ask_ai_manager: AskAiManagerDict
    ask_ai_viewer: AskAiViewerDict
    buy: BuyDict | None
    can_comment: NotRequired[bool]
    can_react_to_collab_comments: bool
    can_request_team_role_upgrade: CanRequestTeamRoleUpgradeDict
    can_update_privacy_to_public: CanUpdatePrivacyToPublicDict
    channel: Channel1Dict
    create_editor: CreateEditorDict
    delete: DeleteDict
    edit: EditDict
    edit_privacy: EditPrivacyDict
    flag_clip: NotRequired[bool]
    has_restricted_privacy_options: HasRestrictedPrivacyOptionsDict
    highlights: HighlightsDict
    interact: NotRequired[bool]
    invite: InviteDict
    legal_hold: LegalHoldDict
    like: LikeDict
    lms_export: NotRequired[Any]
    rent: RentDict | None
    report: Report1Dict
    set_content_rating: SetContentRatingDict
    subscribe: NotRequired[SubscribeDict | None]
    summary: SummaryDict
    text_translations: TextTranslationsDict
    transcript_video_editor: TranscriptVideoEditorDict
    translations: TranslationsDict
    trim: TrimDict
    validate_value: ValidateDict
    view_privacy: ViewPrivacyDict
    view_team_members: ViewTeamMembersDict
    watched: WatchedDict
    watchlater: Watchlater1Dict
