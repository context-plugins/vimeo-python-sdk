from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ConversationsRenamesuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.rename method"""

    channel: Any
    ok: Literal["True"] = "True"


class ConversationsRenamesuccessschemaDict(TypedDict):
    channel: Any
    ok: NotRequired[Literal["True"]]
