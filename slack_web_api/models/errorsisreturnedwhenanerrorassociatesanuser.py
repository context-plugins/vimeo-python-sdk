from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_invite_error_enum import ConversationsInviteErrorEnumOrStr


class Errorsisreturnedwhenanerrorassociatesanuser(SdkBaseModel):
    error: ConversationsInviteErrorEnumOrStr
    ok: Literal["False"] = "False"
    user: Optional[str] = UNSET


class ErrorsisreturnedwhenanerrorassociatesanuserDict(TypedDict):
    error: ConversationsInviteErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
    user: NotRequired[str]
