from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.users_profile_get_error_enum import UsersProfileGetErrorEnumOrStr


class UsersProfileGeterrorschema1(SdkBaseModel):
    """Schema for error response from users.profile.get method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsersProfileGetErrorEnumOrStr
    ok: Literal["False"] = "False"


class UsersProfileGeterrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: UsersProfileGetErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
