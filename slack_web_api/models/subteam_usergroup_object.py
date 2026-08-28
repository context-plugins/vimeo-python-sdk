from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .prefs import Prefs, PrefsDict


class SubteamUsergroupObject(SdkBaseModel):
    auto_provision: bool
    auto_type: Any
    channel_count: Optional[int] = UNSET
    created_by: str
    date_create: int
    date_delete: int
    date_update: int
    deleted_by: Any
    description: str
    enterprise_subteam_id: str
    handle: str
    id: str
    is_external: bool
    is_subteam: bool
    is_usergroup: bool
    name: str
    prefs: Prefs
    team_id: str
    updated_by: str
    user_count: Optional[int] = UNSET
    users: Optional[list[str]] = UNSET


class SubteamUsergroupObjectDict(TypedDict):
    auto_provision: bool
    auto_type: Any
    channel_count: NotRequired[int]
    created_by: str
    date_create: int
    date_delete: int
    date_update: int
    deleted_by: Any
    description: str
    enterprise_subteam_id: str
    handle: str
    id: str
    is_external: bool
    is_subteam: bool
    is_usergroup: bool
    name: str
    prefs: Prefs | PrefsDict
    team_id: str
    updated_by: str
    user_count: NotRequired[int]
    users: NotRequired[list[str]]
