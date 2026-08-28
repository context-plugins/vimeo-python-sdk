from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.users_profile_set_error_enum import UsersProfileSetErrorEnumOrStr


class UsersProfileSeterrorschema1Error(SdkBaseModel):
    """Schema for error response from users.profile.set method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsersProfileSetErrorEnumOrStr
    ok: Literal["False"] = "False"


class UsersProfileSeterrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: UsersProfileSetErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
