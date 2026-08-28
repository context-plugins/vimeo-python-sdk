from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reactions_list_error_enum import ReactionsListErrorEnumOrStr


class ReactionsListerrorschema1Error(SdkBaseModel):
    """Schema for error response from reactions.list method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ReactionsListErrorEnumOrStr
    ok: Literal["False"] = "False"


class ReactionsListerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: ReactionsListErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
