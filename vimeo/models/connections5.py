from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ancestor_path1 import AncestorPath1, AncestorPath1Dict
from .data_retention import DataRetention, DataRetentionDict
from .folders import Folders, FoldersDict
from .group_folder_grants import GroupFolderGrants, GroupFolderGrantsDict
from .items import Items, ItemsDict
from .parent_folder import ParentFolder, ParentFolderDict
from .personal_team_folder_owner import PersonalTeamFolderOwner, PersonalTeamFolderOwnerDict
from .resource_creator_team_user1 import ResourceCreatorTeamUser1, ResourceCreatorTeamUser1Dict
from .team_permissions1 import TeamPermissions1, TeamPermissions1Dict
from .user_folder_access_grants import UserFolderAccessGrants, UserFolderAccessGrantsDict
from .videos5 import Videos5, Videos5Dict


class Connections5(SdkBaseModel):
    """A list of resource URIs related to the folder."""

    ancestor_path: list[AncestorPath1]
    """Information about the folder's ancestry ordered from the direct parent to higher-level ancestors."""

    data_retention: DataRetention
    folders: Folders
    """A standard connection object indicating how to return all the subfolders in the folder."""

    group_folder_grants: GroupFolderGrants
    """Information about the folder's group access grants."""

    items: Items
    """A standard connection object indicating how to return all the items in the folder."""

    parent_folder: ParentFolder
    """A standard connection object indicating how to return the folder's parent folder."""

    personal_team_folder_owner: PersonalTeamFolderOwner
    """Information about the owner of the personal team folder."""

    resource_creator_team_user: ResourceCreatorTeamUser1
    """Information about the team user who created the folder. This data requires a bearer token with the ``private``
    scope."""

    team_permissions: TeamPermissions1
    """Information about the folder's team permissions list. This data requires a bearer token with the ``private``
    scope."""

    user_folder_access_grants: UserFolderAccessGrants
    """Information about the folder's user folder access grants."""

    videos: Videos5
    """A standard connection object indicating how to return all the videos in the folder."""


class Connections5Dict(TypedDict):
    ancestor_path: list[AncestorPath1 | AncestorPath1Dict]
    data_retention: DataRetention | DataRetentionDict
    folders: Folders | FoldersDict
    group_folder_grants: GroupFolderGrants | GroupFolderGrantsDict
    items: Items | ItemsDict
    parent_folder: ParentFolder | ParentFolderDict
    personal_team_folder_owner: PersonalTeamFolderOwner | PersonalTeamFolderOwnerDict
    resource_creator_team_user: ResourceCreatorTeamUser1 | ResourceCreatorTeamUser1Dict
    team_permissions: TeamPermissions1 | TeamPermissions1Dict
    user_folder_access_grants: UserFolderAccessGrants | UserFolderAccessGrantsDict
    videos: Videos5 | Videos5Dict
