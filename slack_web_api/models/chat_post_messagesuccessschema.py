from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .messageobject import Messageobject, MessageobjectDict


class ChatPostMessagesuccessschema(SdkBaseModel):
    """Schema for successful response of chat.postMessage method"""

    channel: str
    message: Messageobject
    ok: Literal["True"] = "True"
    ts: str


class ChatPostMessagesuccessschemaDict(TypedDict):
    channel: str
    message: Messageobject | MessageobjectDict
    ok: NotRequired[Literal["True"]]
    ts: str
