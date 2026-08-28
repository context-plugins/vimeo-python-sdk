from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.apps_permissions_resources_list_error_enum import AppsPermissionsResourcesListErrorEnumOrStr


class AppsPermissionsResourcesListerrorschema1Error(SdkBaseModel):
    """Schema for error response from apps.permissions.resources.list method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: AppsPermissionsResourcesListErrorEnumOrStr
    ok: Literal["False"] = "False"


class AppsPermissionsResourcesListerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: AppsPermissionsResourcesListErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
