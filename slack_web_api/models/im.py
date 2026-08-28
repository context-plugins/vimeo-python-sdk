from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .resourcesininfofromapps_permissions_info import (
    ResourcesininfofromappsPermissionsInfo,
    ResourcesininfofromappsPermissionsInfoDict,
)


class Im(SdkBaseModel):
    resources: Optional[ResourcesininfofromappsPermissionsInfo] = UNSET
    scopes: Optional[list[str]] = UNSET


class ImDict(TypedDict):
    resources: NotRequired[ResourcesininfofromappsPermissionsInfo | ResourcesininfofromappsPermissionsInfoDict]
    scopes: NotRequired[list[str]]
