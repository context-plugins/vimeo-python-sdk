from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.users_list_error_enum import UsersListErrorEnumOrStr


class UsersListerrorschema1Error(SdkBaseModel):
    """Schema for error response from users.list method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsersListErrorEnumOrStr
    ok: Literal["False"] = "False"


class UsersListerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: UsersListErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
