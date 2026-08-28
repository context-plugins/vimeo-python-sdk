from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ConversationsSetTopicsuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.setTopic method"""

    channel: Any
    ok: Literal["True"] = "True"


class ConversationsSetTopicsuccessschemaDict(TypedDict):
    channel: Any
    ok: NotRequired[Literal["True"]]
