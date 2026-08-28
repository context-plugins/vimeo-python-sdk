from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.usergroups_update_error_enum import UsergroupsUpdateErrorEnumOrStr


class UsergroupsUsersUpdateerrorschema1Error(SdkBaseModel):
    """Schema for error response from usergroups.users.update method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsergroupsUpdateErrorEnumOrStr
    ok: Literal["False"] = "False"


class UsergroupsUsersUpdateerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: UsergroupsUpdateErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
