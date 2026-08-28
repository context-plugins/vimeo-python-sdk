from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.usergroups_create_error_enum import UsergroupsCreateErrorEnumOrStr


class UsergroupsCreateerrorschema1(SdkBaseModel):
    """Schema for error response from usergroups.create method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsergroupsCreateErrorEnumOrStr
    ok: Literal["False"] = "False"


class UsergroupsCreateerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: UsergroupsCreateErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
