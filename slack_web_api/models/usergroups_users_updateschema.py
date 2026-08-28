from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .subteam_usergroup_object import SubteamUsergroupObject, SubteamUsergroupObjectDict


class UsergroupsUsersUpdateschema(SdkBaseModel):
    """Schema for successful response from usergroups.users.update method"""

    ok: Literal["True"] = "True"
    usergroup: SubteamUsergroupObject


class UsergroupsUsersUpdateschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    usergroup: SubteamUsergroupObject | SubteamUsergroupObjectDict
