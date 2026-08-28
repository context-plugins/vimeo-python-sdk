from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ConversationsSetPurposesuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.setPurpose method"""

    channel: Any
    ok: Literal["True"] = "True"


class ConversationsSetPurposesuccessschemaDict(TypedDict):
    channel: Any
    ok: NotRequired[Literal["True"]]
