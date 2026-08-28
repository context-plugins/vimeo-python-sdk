from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.apps_permissions_request_error_enum import AppsPermissionsRequestErrorEnumOrStr


class AppsPermissionsRequesterrorschema1(SdkBaseModel):
    """Schema for error response from apps.permissions.request method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: AppsPermissionsRequestErrorEnumOrStr
    ok: Literal["False"] = "False"


class AppsPermissionsRequesterrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: AppsPermissionsRequestErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
