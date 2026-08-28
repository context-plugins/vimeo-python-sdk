from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .messageobject1 import Messageobject1, Messageobject1Dict


class ChatUpdatesuccessschema(SdkBaseModel):
    """Schema for successful response of chat.update method"""

    channel: str
    message: Messageobject1
    ok: Literal["True"] = "True"
    text: str
    ts: str


class ChatUpdatesuccessschemaDict(TypedDict):
    channel: str
    message: Messageobject1 | Messageobject1Dict
    ok: NotRequired[Literal["True"]]
    text: str
    ts: str
