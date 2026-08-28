from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.users_info_error_enum import UsersInfoErrorEnumOrStr


class UsersInfoerrorschema1Error(SdkBaseModel):
    """Schema for error response from users.info method"""

    callstack: Optional[str] = UNSET
    error: UsersInfoErrorEnumOrStr
    ok: Literal["False"] = "False"


class UsersInfoerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: UsersInfoErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
