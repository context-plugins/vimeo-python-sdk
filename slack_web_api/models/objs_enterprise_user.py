from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ObjsEnterpriseUser(SdkBaseModel):
    enterprise_id: str
    enterprise_name: str
    id: str
    is_admin: bool
    is_owner: bool
    teams: list[str]


class ObjsEnterpriseUserDict(TypedDict):
    enterprise_id: str
    enterprise_name: str
    id: str
    is_admin: bool
    is_owner: bool
    teams: list[str]
