from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .applicable_permission_policies import ApplicablePermissionPolicies, ApplicablePermissionPoliciesDict
from .enums.permission_level1 import PermissionLevel1OrStr
from .enums.status21 import Status21OrStr
from .metadata26 import Metadata26, Metadata26Dict
from .team_role import TeamRole, TeamRoleDict
from .user import User, UserDict


class TeamMembership(SdkBaseModel):
    access_grant: Any | None
    """Information about an access grant that applies to the team member on the folder. _This field is deprecated
    because grants are no longer exposed via API responses._"""

    active: bool
    """Whether the team membership is currently active."""

    applicable_permission_policies: ApplicablePermissionPolicies
    """Information about permission policies that can apply to the team member."""

    applicable_roles: list[TeamRole]
    """An array of the team roles this team member can have."""

    created_time: str
    """The time in ISO 8601 format when the invite was sent."""

    email: str
    """The team member's email."""

    exclude_sso: bool | None
    """Whether the team member should be excluded from single sign-on."""

    has_folder_access: Optional[bool] = UNSET
    """Whether the team member has folder access."""

    has_lms_user: Optional[bool] = UNSET
    """Whether the team member has an LMS user."""

    invite_url: str | None
    """The URL for the invited user to join the team. The value of this field is null if the invited user has already
    joined."""

    joined_time: str
    """The time in ISO 8601 format when the invite was accepted."""

    metadata: Metadata26
    """The metadata of the team membership."""

    modified_time: str
    """The time in ISO 8601 format when the team membership was last modified."""

    permission_actions: list[str]
    """The allowable permission actions of the team user."""

    permission_level: PermissionLevel1OrStr
    """The team member's permission level.

    Option descriptions:
     * ``Admin`` - The team member has admin permissions. They can upload and edit videos for the entire team and
            perform team administration tasks.
     * ``Contributor`` - The team member has contributor permissions. They can upload and edit videos for the entire
            team but can't perform team administration tasks.
     * ``Contributor Plus`` - The team member has contributor plus permissions. They can upload and edit videos for the
            entire team, and have additional sets of permissions, but can't perform team administration tasks.
     * ``Owner`` - The team member has owner permissions.
     * ``Uploader`` - The team member has uploader permissions. They can upload videos for the entire team but can't
            edit videos.
     * ``Viewer`` - The team member has viewer permissions. They can access team videos and specific team folders but
            can't upload or edit videos."""

    recently_reminded: Optional[bool] = UNSET
    """Whether the team member has been reminded about the invite."""

    resource_key: str
    """The resource key of the team membership."""

    role: str
    """The team member's role, translated."""

    status: Status21OrStr
    """The status of the team membership invite.

    Option descriptions:
     * ``accepted`` - Team membership has been accepted.
     * ``pending`` - Team membership has been offered but not yet accepted."""

    uri: str
    """The URI of the team membership resource."""

    user: User | None
    """The team member. The value of this field is null if the user hasn't joined the team yet."""


class TeamMembershipDict(TypedDict):
    access_grant: Any | None
    active: bool
    applicable_permission_policies: ApplicablePermissionPolicies | ApplicablePermissionPoliciesDict
    applicable_roles: list[TeamRole | TeamRoleDict]
    created_time: str
    email: str
    exclude_sso: bool | None
    has_folder_access: NotRequired[bool]
    has_lms_user: NotRequired[bool]
    invite_url: str | None
    joined_time: str
    metadata: Metadata26 | Metadata26Dict
    modified_time: str
    permission_actions: list[str]
    permission_level: PermissionLevel1OrStr
    recently_reminded: NotRequired[bool]
    resource_key: str
    role: str
    status: Status21OrStr
    uri: str
    user: User | UserDict | None
