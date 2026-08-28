from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dnd_end_dnd_error_enum import DndEndDndErrorEnumOrStr


class DndEndDnderrorschema1Error(SdkBaseModel):
    """Schema for error response from dnd.endDnd method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: DndEndDndErrorEnumOrStr
    ok: Literal["False"] = "False"


class DndEndDnderrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: DndEndDndErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
