from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .subteam_usergroup_object import SubteamUsergroupObject, SubteamUsergroupObjectDict


class UsergroupsEnableschema(SdkBaseModel):
    """Schema for successful response from usergroups.enable method"""

    ok: Literal["True"] = "True"
    usergroup: SubteamUsergroupObject


class UsergroupsEnableschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    usergroup: SubteamUsergroupObject | SubteamUsergroupObjectDict
