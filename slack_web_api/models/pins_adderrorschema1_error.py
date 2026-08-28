from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pins_add_error_enum import PinsAddErrorEnumOrStr


class PinsAdderrorschema1Error(SdkBaseModel):
    """Schema for error response from pins.add method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: PinsAddErrorEnumOrStr
    ok: Literal["False"] = "False"


class PinsAdderrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: PinsAddErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
