from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_dictionary_quota import AccountDictionaryQuota, AccountDictionaryQuotaDict
from .ai_credits_quota import AiCreditsQuota, AiCreditsQuotaDict
from .bandwidth import Bandwidth, BandwidthDict
from .drm_licenses_quota import DrmLicensesQuota, DrmLicensesQuotaDict
from .enums.age_verification_status import AgeVerificationStatusOrStr
from .enums.content_filter import ContentFilterOrStr
from .lms_learner_seats_quota import LmsLearnerSeatsQuota, LmsLearnerSeatsQuotaDict
from .location import Location, LocationDict
from .membership import Membership, MembershipDict
from .metadata3 import Metadata3, Metadata3Dict
from .picture import Picture, PictureDict
from .preferences import Preferences, PreferencesDict
from .skill import Skill, SkillDict
from .upload_quota import UploadQuota, UploadQuotaDict
from .website import Website, WebsiteDict


class User(SdkBaseModel):
    account_dictionary_quota: Optional[AccountDictionaryQuota] = UNSET
    """Account dictionary usage and entry limits."""

    age_verification_status: AgeVerificationStatusOrStr
    """The status of the user's age verification.

    Option descriptions:
     * ``failed`` - The user has failed age verification.
     * ``passed`` - The user has passed age verification.
     * ``pending`` - The user's age verification is pending."""

    ai_credits_quota: Optional[AiCreditsQuota] = UNSET
    """Information about the user's AI credits quota."""

    available_for_hire: bool
    """Whether the authenticated user is available for hire."""

    bandwidth: Optional[Bandwidth] = UNSET
    bio: Optional[str] = UNSET
    """The authenticated user's long biography text."""

    can_work_remotely: bool
    """Whether the authenticated user can work remotely."""

    capabilities: Optional[Any] = UNSET
    """The users's capabilities list."""

    clients: str
    """The comma-separated list of clients."""

    content_filter: Optional[ContentFilterOrStr] = UNSET
    """The authenticated user's content filters.

    Option descriptions:
     * ``drugs`` - The content contains drug or alcohol use.
     * ``language`` - The content contains profanity or sexually suggestive language.
     * ``nudity`` - The content contains nudity.
     * ``safe`` - The content is suitable for all audiences.
     * ``unrated`` - The content hasn't been rated.
     * ``violence`` - The content contains violence or is graphic."""

    created_time: str
    """The time in ISO 8601 format when the user account was created."""

    drm_licenses_quota: Optional[DrmLicensesQuota] = UNSET
    """Information about the user's DRM usage quota."""

    gender: Optional[str] = UNSET
    """The authenticated user's gender."""

    has_invalid_email: Optional[bool] = UNSET
    """Whether the user's email is invalid."""

    is_expert: bool
    """Whether the creator enrolled in and successfully completed the Vimeo Experts program."""

    is_staff_picked: bool
    """Whether the user has had a staff-picked video."""

    last_video_upload_date: Optional[str] = UNSET
    """The time in ISO 8601 format of the user's most recent video upload, or null if the user has no videos. Backed by
    a lean, indexed clip lookup cached for one hour."""

    link: str
    """The absolute URL of the authenticated users's profile page."""

    live_localization_trial_expires_on: Optional[str] = UNSET
    """When the user's access to the exclusive live-localization features (caption translations, multi-audio streams)
    comes from the launch free trial, the date (YYYY-MM-DD) the trial expires. Null for users with permanent access
    (staff or a granted SKU) or no trial."""

    lms_learner_seats_quota: Optional[LmsLearnerSeatsQuota] = UNSET
    """Information about the user's learning management system learner seats quota."""

    location: Optional[str] = UNSET
    """The authenticated user's location."""

    location_details: Optional[Location] = UNSET
    """The authenticated user's location details."""

    max_team_members: float
    """The maximum number of team members the user may have."""

    membership: Membership
    """Information about the authenticated user's Vimeo membership."""

    metadata: Metadata3
    """The authenticated user's metadata."""

    name: str
    """The authenticated user's display name."""

    pictures: Picture
    """The active portrait of the authenticated user."""

    preferences: Preferences
    profile_discovery: bool
    """Whether the user has enabled profile discovery from their profile settings."""

    requires_age_verification: bool
    """Whether the user is required to verify their age."""

    resource_key: str
    """The authenticated user's resource key string."""

    short_bio: Optional[str] = UNSET
    """The authenticated user's short biography text."""

    skills: Optional[list[Skill]] = UNSET
    """A list of the authenticated user's skills."""

    transcript_phrases_limit: Optional[float] = UNSET
    """The maximum number of transcript phrases permitted for the user."""

    upload_quota: UploadQuota
    """The upload quota. This information appears only when the authenticated user has upload access and is looking at
    their own user record."""

    uri: str
    """The authenticated user's canonical relative URI."""

    websites: list[Website]
    """The authenticated user's websites."""


class UserDict(TypedDict):
    account_dictionary_quota: NotRequired[AccountDictionaryQuota | AccountDictionaryQuotaDict]
    age_verification_status: AgeVerificationStatusOrStr
    ai_credits_quota: NotRequired[AiCreditsQuota | AiCreditsQuotaDict]
    available_for_hire: bool
    bandwidth: NotRequired[Bandwidth | BandwidthDict]
    bio: NotRequired[str]
    can_work_remotely: bool
    capabilities: NotRequired[Any]
    clients: str
    content_filter: NotRequired[ContentFilterOrStr]
    created_time: str
    drm_licenses_quota: NotRequired[DrmLicensesQuota | DrmLicensesQuotaDict]
    gender: NotRequired[str]
    has_invalid_email: NotRequired[bool]
    is_expert: bool
    is_staff_picked: bool
    last_video_upload_date: NotRequired[str]
    link: str
    live_localization_trial_expires_on: NotRequired[str]
    lms_learner_seats_quota: NotRequired[LmsLearnerSeatsQuota | LmsLearnerSeatsQuotaDict]
    location: NotRequired[str]
    location_details: NotRequired[Location | LocationDict]
    max_team_members: float
    membership: Membership | MembershipDict
    metadata: Metadata3 | Metadata3Dict
    name: str
    pictures: Picture | PictureDict
    preferences: Preferences | PreferencesDict
    profile_discovery: bool
    requires_age_verification: bool
    resource_key: str
    short_bio: NotRequired[str]
    skills: NotRequired[list[Skill | SkillDict]]
    transcript_phrases_limit: NotRequired[float]
    upload_quota: UploadQuota | UploadQuotaDict
    uri: str
    websites: list[Website | WebsiteDict]
