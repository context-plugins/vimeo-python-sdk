from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .metadata5 import Metadata5, Metadata5Dict
from .privacy2 import Privacy2, Privacy2Dict
from .review_link import ReviewLink, ReviewLinkDict
from .settings import Settings, SettingsDict
from .user import User, UserDict


class Project(SdkBaseModel):
    access_grant: Any
    """The access grant response that applies to the team member. _This field is deprecated because grants are no longer
    exposed via API responses._"""

    created_time: str
    """The time in ISO 8601 format when the folder was created."""

    creator_uri: str
    """The URI for the user who created the folder."""

    has_subfolder: bool
    """Whether this folder has at least one subfolder."""

    is_pinned: bool
    """Whether the folder is pinned."""

    is_private_to_user: bool
    """Whether the folder is a private-to-me folder for the user."""

    is_starred_by_cur_user: bool
    """Whether the current user has starred this folder."""

    last_user_action_event_date: str | None
    """The time in ISO 8601 format when a user last performed an action on the folder."""

    link: str
    """The link to the folder on Vimeo."""

    manage_link: str
    """The link to the folder management page."""

    metadata: Metadata5
    """Information about the folders's metadata."""

    modified_time: str
    """The time in ISO 8601 format when the folder was last modified."""

    name: str
    """The name of the folder."""

    pinned_on: str | None
    """The time in ISO 8601 format when the folder was pinned."""

    privacy: Privacy2
    """The privacy settings of the folder."""

    resource_key: str
    """The resource key string of the folder."""

    review_links: Optional[list[ReviewLink]] = UNSET
    """All active review links associated with the folder."""

    settings: Settings
    """The settings of the folder."""

    should_show_team_library_notification: bool
    """Whether to display a folder notification that directs the current user to the team library page."""

    uri: str
    """The URI of the folder."""

    user: User
    """The owner of the folder."""


class ProjectDict(TypedDict):
    access_grant: Any
    created_time: str
    creator_uri: str
    has_subfolder: bool
    is_pinned: bool
    is_private_to_user: bool
    is_starred_by_cur_user: bool
    last_user_action_event_date: str | None
    link: str
    manage_link: str
    metadata: Metadata5Dict
    modified_time: str
    name: str
    pinned_on: str | None
    privacy: Privacy2Dict
    resource_key: str
    review_links: NotRequired[list[ReviewLinkDict]]
    settings: SettingsDict
    should_show_team_library_notification: bool
    uri: str
    user: UserDict
