from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.rtm_connect_error_enum import RtmConnectErrorEnumOrStr


class RtmConnecterrorschema1(SdkBaseModel):
    """Schema for error response from rtm.connect method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: RtmConnectErrorEnumOrStr
    ok: Literal["False"] = "False"


class RtmConnecterrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: RtmConnectErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
