from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bots_info_error_enum import BotsInfoErrorEnumOrStr


class BotsInfoerrorschema1(SdkBaseModel):
    """Schema for error response from bots.info method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: BotsInfoErrorEnumOrStr
    ok: Literal["False"] = "False"


class BotsInfoerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: BotsInfoErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
