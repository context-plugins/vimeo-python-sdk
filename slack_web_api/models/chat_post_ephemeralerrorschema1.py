from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.chat_post_ephemeral_error_enum import ChatPostEphemeralErrorEnumOrStr


class ChatPostEphemeralerrorschema1(SdkBaseModel):
    """Schema for error response from chat.postEphemeral method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: ChatPostEphemeralErrorEnumOrStr
    ok: Literal["False"] = "False"


class ChatPostEphemeralerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: ChatPostEphemeralErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
