from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ChatDeletesuccessschema(SdkBaseModel):
    """Schema for successful response of chat.delete method"""

    channel: str
    ok: Literal["True"] = "True"
    ts: str


class ChatDeletesuccessschemaDict(TypedDict):
    channel: str
    ok: NotRequired[Literal["True"]]
    ts: str
