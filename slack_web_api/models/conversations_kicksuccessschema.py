from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ConversationsKicksuccessschema(SdkBaseModel):
    """Schema for successful response conversations.kick method"""

    ok: Literal["True"] = "True"


class ConversationsKicksuccessschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
