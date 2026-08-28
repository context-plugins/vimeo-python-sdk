from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.auth_test_error_enum import AuthTestErrorEnumOrStr


class AuthTesterrorschema1Error(SdkBaseModel):
    """Schema for error response auth.test method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: AuthTestErrorEnumOrStr
    ok: Literal["False"] = "False"


class AuthTesterrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: AuthTestErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
