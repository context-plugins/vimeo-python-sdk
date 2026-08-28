from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.usergroups_create_error_enum import UsergroupsCreateErrorEnumOrStr


class UsergroupsDisableerrorschema1Error(SdkBaseModel):
    """Schema for error response from usergroups.disable method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsergroupsCreateErrorEnumOrStr
    ok: Literal["False"] = "False"


class UsergroupsDisableerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: UsergroupsCreateErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
