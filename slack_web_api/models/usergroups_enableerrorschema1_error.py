from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.usergroups_enable_error_enum import UsergroupsEnableErrorEnumOrStr


class UsergroupsEnableerrorschema1Error(SdkBaseModel):
    """Schema for error response from usergroups.enable method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsergroupsEnableErrorEnumOrStr
    ok: Literal["False"] = "False"


class UsergroupsEnableerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: UsergroupsEnableErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
