from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reactions_add_error_enum import ReactionsAddErrorEnumOrStr


class ReactionsAdderrorschema1(SdkBaseModel):
    """Schema for error response from reactions.add method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ReactionsAddErrorEnumOrStr
    ok: Literal["False"] = "False"


class ReactionsAdderrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ReactionsAddErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
