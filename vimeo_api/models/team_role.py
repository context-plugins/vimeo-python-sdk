from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .applicable_permission_policies1 import ApplicablePermissionPolicies1, ApplicablePermissionPolicies1Dict
from .enums.permission_level import PermissionLevelOrStr
from .enums.role import RoleOrStr


class TeamRole(SdkBaseModel):
    applicable_permission_policies: Optional[ApplicablePermissionPolicies1] = UNSET
    """The applicable permission policies for the role."""

    count: Optional[float] = UNSET
    """The total number of team members with this role."""

    display_description: Optional[str] = UNSET
    """The translated display description of the role."""

    display_name: Optional[str] = UNSET
    """The translated display name of the role."""

    is_disabled: Optional[bool] = UNSET
    """Whether the role is disabled for certain team members."""

    permission_level: PermissionLevelOrStr | None
    """The untranslated role of the user who made the request.

    Option descriptions:
     * ``Admin`` - The team member has admin permissions. They can upload and edit videos for the entire team and
            perform team administration tasks.
     * ``Contributor`` - The team member has contributor permissions. They can upload and edit videos for the entire
            team but can’t perform team administration tasks.
     * ``Contributor Plus`` - The team member has contributor-plus permissions. They can upload and edit videos for the
            entire team and have additional sets of permissions but can't perform team administration tasks.
     * ``Owner`` - The team member has owner permissions.
     * ``Uploader`` - The team member has uploader permissions. They can upload videos for the entire team but can't
            edit videos.
     * ``Viewer`` - The team member has viewer permissions. They can access team videos and specific team folders but
            can't upload or edit videos."""

    role: RoleOrStr | None
    """The untranslated role of the user who made the request.

    Option descriptions:
     * ``Admin`` - The team member has admin permissions. They can upload and edit videos for the entire team and
            perform team administration tasks.
     * ``Contributor`` - The team member has contributor permissions. They can upload and edit videos for the entire
            team but can’t perform team administration tasks.
     * ``Contributor Plus`` - The team member has contributor-plus permissions. They can upload and edit videos for the
            entire team and have additional sets of permissions but can't perform team administration tasks.
     * ``Owner`` - The team member has owner permissions.
     * ``Uploader`` - The team member has uploader permissions. They can upload videos for the entire team but can’t
            edit videos.
     * ``Viewer`` - The team member has viewer permissions. They can access team videos and specific team folders but
            can’t upload or edit videos."""

    uri: str
    """The URI of the team role."""


class TeamRoleDict(TypedDict):
    applicable_permission_policies: NotRequired[ApplicablePermissionPolicies1 | ApplicablePermissionPolicies1Dict]
    count: NotRequired[float]
    display_description: NotRequired[str]
    display_name: NotRequired[str]
    is_disabled: NotRequired[bool]
    permission_level: PermissionLevelOrStr | None
    role: RoleOrStr | None
    uri: str
