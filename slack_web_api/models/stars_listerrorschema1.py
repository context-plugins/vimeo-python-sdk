from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.apps_permissions_info_error_enum import AppsPermissionsInfoErrorEnumOrStr


class StarsListerrorschema1(SdkBaseModel):
    """Schema for error response from stars.list method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: AppsPermissionsInfoErrorEnumOrStr
    ok: Literal["False"] = "False"


class StarsListerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: AppsPermissionsInfoErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
