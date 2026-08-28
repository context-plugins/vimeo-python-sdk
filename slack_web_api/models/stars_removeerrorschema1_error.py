from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.stars_remove_error_enum import StarsRemoveErrorEnumOrStr


class StarsRemoveerrorschema1Error(SdkBaseModel):
    """Schema for error response from stars.remove method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: StarsRemoveErrorEnumOrStr
    ok: Literal["False"] = "False"


class StarsRemoveerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: StarsRemoveErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
