from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.users_lookup_by_email_error_enum import UsersLookupByEmailErrorEnumOrStr


class UsersLookupByEmailerrorschema1Error(SdkBaseModel):
    """Schema for error response from users.lookupByEmail method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: UsersLookupByEmailErrorEnumOrStr
    ok: Literal["False"] = "False"


class UsersLookupByEmailerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: UsersLookupByEmailErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
