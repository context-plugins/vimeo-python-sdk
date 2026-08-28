from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pins_list_error_enum import PinsListErrorEnumOrStr


class PinsListerrorschema1(SdkBaseModel):
    """Schema for error response from pins.list method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: PinsListErrorEnumOrStr
    ok: Literal["False"] = "False"


class PinsListerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: PinsListErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
