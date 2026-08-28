from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .resourcesininfofromapps_permissions_info import (
    ResourcesininfofromappsPermissionsInfo,
    ResourcesininfofromappsPermissionsInfoDict,
)


class Team(SdkBaseModel):
    resources: ResourcesininfofromappsPermissionsInfo
    scopes: list[str]


class TeamDict(TypedDict):
    resources: ResourcesininfofromappsPermissionsInfo | ResourcesininfofromappsPermissionsInfoDict
    scopes: list[str]
