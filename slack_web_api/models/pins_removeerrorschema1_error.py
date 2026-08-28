from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pins_remove_error_enum import PinsRemoveErrorEnumOrStr


class PinsRemoveerrorschema1Error(SdkBaseModel):
    """Schema for error response from pins.remove method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: PinsRemoveErrorEnumOrStr
    ok: Literal["False"] = "False"


class PinsRemoveerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: PinsRemoveErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
