from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.users_set_photo_error_enum import UsersSetPhotoErrorEnumOrStr


class UsersSetPhotoerrorschema1Error(SdkBaseModel):
    """Schema for error response from users.setPhoto method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    debug_step: Optional[str] = UNSET
    """possibly DEV/QA only"""

    dims: Optional[str] = UNSET
    """possibly DEV/QA only"""

    error: UsersSetPhotoErrorEnumOrStr
    ok: Literal["False"] = "False"
    time_ident: Optional[int] = UNSET
    """possibly DEV/QA only"""


class UsersSetPhotoerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    debug_step: NotRequired[str]
    dims: NotRequired[str]
    error: UsersSetPhotoErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
    time_ident: NotRequired[int]
