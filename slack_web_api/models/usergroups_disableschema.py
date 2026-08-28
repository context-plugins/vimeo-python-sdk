from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .subteam_usergroup_object import SubteamUsergroupObject, SubteamUsergroupObjectDict


class UsergroupsDisableschema(SdkBaseModel):
    """Schema for successful response from usergroups.disable method"""

    ok: Literal["True"] = "True"
    usergroup: SubteamUsergroupObject


class UsergroupsDisableschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    usergroup: SubteamUsergroupObject | SubteamUsergroupObjectDict
