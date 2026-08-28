from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ChatDeleteScheduledMessageschema(SdkBaseModel):
    """Schema for successful response from chat.deleteScheduledMessage method"""

    ok: Literal["True"] = "True"


class ChatDeleteScheduledMessageschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
