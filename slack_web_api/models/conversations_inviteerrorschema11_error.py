from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.conversations_invite_error_enum import ConversationsInviteErrorEnumOrStr
from .errorsisreturnedwhenanerrorassociatesanuser import (
    Errorsisreturnedwhenanerrorassociatesanuser,
    ErrorsisreturnedwhenanerrorassociatesanuserDict,
)


class ConversationsInviteerrorschema11Error(SdkBaseModel):
    """Schema for error response from conversations.invite method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: Optional[ConversationsInviteErrorEnumOrStr] = UNSET
    errors: Optional[list[Errorsisreturnedwhenanerrorassociatesanuser]] = UNSET
    needed: Optional[str] = UNSET
    ok: Literal["False"] = "False"
    provided: Optional[str] = UNSET


class ConversationsInviteerrorschema11ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: NotRequired[ConversationsInviteErrorEnumOrStr]
    errors: NotRequired[
        list[Errorsisreturnedwhenanerrorassociatesanuser | ErrorsisreturnedwhenanerrorassociatesanuserDict]
    ]
    needed: NotRequired[str]
    ok: NotRequired[Literal["False"]]
    provided: NotRequired[str]
