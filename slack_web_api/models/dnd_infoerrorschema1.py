from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dnd_info_error_enum import DndInfoErrorEnumOrStr


class DndInfoerrorschema1(SdkBaseModel):
    """Schema for error response from dnd.info method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: DndInfoErrorEnumOrStr
    ok: Literal["False"] = "False"


class DndInfoerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: DndInfoErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
