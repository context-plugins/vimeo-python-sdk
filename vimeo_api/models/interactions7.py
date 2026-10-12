from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .add_custom_thumbnails import AddCustomThumbnails, AddCustomThumbnailsDict
from .add_live_events import AddLiveEvents, AddLiveEventsDict
from .add_logos import AddLogos, AddLogosDict
from .add_to1 import AddTo1, AddTo1Dict
from .add_videos import AddVideos, AddVideosDict
from .can_update_privacy_to_public1 import CanUpdatePrivacyToPublic1, CanUpdatePrivacyToPublic1Dict
from .delete2 import Delete2, Delete2Dict
from .edit2 import Edit2, Edit2Dict
from .edit_live_events import EditLiveEvents, EditLiveEventsDict
from .invite3 import Invite3, Invite3Dict
from .view_privacy1 import ViewPrivacy1, ViewPrivacy1Dict


class Interactions7(SdkBaseModel):
    """A list of resource URIs related to the showcase."""

    add_custom_thumbnails: AddCustomThumbnails
    """An action indicating that the authenticated user is an administrator of the showcase and may therefore add custom
    thumbnails. This data requires a bearer token with the ``private`` scope."""

    add_live_events: AddLiveEvents
    """An action indicating that the authenticated user is an administrator of the showcase and may therefore add
    events. This data requires a bearer token with the ``private`` scope."""

    add_logos: AddLogos
    """An action indicating that the authenticated user is an administrator of the showcase and may therefore add custom
    logos. This data requires a bearer token with the ``private`` scope."""

    add_to: AddTo1 | None
    """Information about adding or removing a video from the showcase. This data requires a bearer token with the
    ``private`` scope."""

    add_videos: AddVideos
    """An action indicating that the authenticated user is an administrator of the showcase and may therefore add
    videos. This data requires a bearer token with the ``private`` scope."""

    can_update_privacy_to_public: CanUpdatePrivacyToPublic1
    """Whether the user can update the showcase privacy to public."""

    delete: Delete2 | None
    """Information about where and how to delete a showcase."""

    edit: Edit2 | None
    """Information about where and how to edit a showcase."""

    edit_live_events: EditLiveEvents
    """An action indicating that the authenticated user can edit event videos inside the showcase. This data requires a
    bearer token with the ``private`` scope."""

    invite: Invite3 | None
    """Information about where and how to invite a team member to a showcase."""

    view_privacy: ViewPrivacy1 | None
    """Information about whether a user has permissions to view the privacy of the showcase."""


class Interactions7Dict(TypedDict):
    add_custom_thumbnails: AddCustomThumbnailsDict
    add_live_events: AddLiveEventsDict
    add_logos: AddLogosDict
    add_to: AddTo1Dict | None
    add_videos: AddVideosDict
    can_update_privacy_to_public: CanUpdatePrivacyToPublic1Dict
    delete: Delete2Dict | None
    edit: Edit2Dict | None
    edit_live_events: EditLiveEventsDict
    invite: Invite3Dict | None
    view_privacy: ViewPrivacy1Dict | None
