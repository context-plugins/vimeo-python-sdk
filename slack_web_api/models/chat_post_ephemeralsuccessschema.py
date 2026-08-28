from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ChatPostEphemeralsuccessschema(SdkBaseModel):
    """Schema for successful response from chat.postEphemeral method"""

    message_ts: str
    ok: Literal["True"] = "True"


class ChatPostEphemeralsuccessschemaDict(TypedDict):
    message_ts: str
    ok: NotRequired[Literal["True"]]
