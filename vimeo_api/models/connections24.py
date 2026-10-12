from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .groups2 import Groups2, Groups2Dict
from .owner1 import Owner1, Owner1Dict
from .personal_team_folder import PersonalTeamFolder, PersonalTeamFolderDict


class Connections24(SdkBaseModel):
    """A list of resource URIs related to the user."""

    groups: Groups2
    """A standard connection object indicating how to return groups that this team user is a part of."""

    owner: Owner1
    """Information about the team owner."""

    personal_team_folder: PersonalTeamFolder
    """A standard connection object indicating how to return personal team folders."""


class Connections24Dict(TypedDict):
    groups: Groups2Dict
    owner: Owner1Dict
    personal_team_folder: PersonalTeamFolderDict
