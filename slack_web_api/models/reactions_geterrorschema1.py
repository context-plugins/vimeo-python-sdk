from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reactions_get_error_enum import ReactionsGetErrorEnumOrStr


class ReactionsGeterrorschema1(SdkBaseModel):
    """Schema for error response from reactions.get method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ReactionsGetErrorEnumOrStr
    ok: Literal["False"] = "False"


class ReactionsGeterrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ReactionsGetErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
