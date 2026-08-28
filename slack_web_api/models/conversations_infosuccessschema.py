from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ConversationsInfosuccessschema(SdkBaseModel):
    """Schema for successful response conversations.info"""

    channel: Any
    ok: Literal["True"] = "True"


class ConversationsInfosuccessschemaDict(TypedDict):
    channel: Any
    ok: NotRequired[Literal["True"]]
