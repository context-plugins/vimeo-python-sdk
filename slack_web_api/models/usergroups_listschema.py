from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .subteam_usergroup_object import SubteamUsergroupObject, SubteamUsergroupObjectDict


class UsergroupsListschema(SdkBaseModel):
    """Schema for successful response from usergroups.list method"""

    ok: Literal["True"] = "True"
    usergroups: list[SubteamUsergroupObject]


class UsergroupsListschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    usergroups: list[SubteamUsergroupObject | SubteamUsergroupObjectDict]
