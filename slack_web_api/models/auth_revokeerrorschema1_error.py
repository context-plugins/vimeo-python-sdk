from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.auth_revoke_error_enum import AuthRevokeErrorEnumOrStr


class AuthRevokeerrorschema1Error(SdkBaseModel):
    """Schema for error response from auth.revoke method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: AuthRevokeErrorEnumOrStr
    ok: Literal["False"] = "False"


class AuthRevokeerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: AuthRevokeErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
