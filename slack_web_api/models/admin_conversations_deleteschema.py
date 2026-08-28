from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AdminConversationsDeleteschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.delete"""

    ok: Literal["True"] = "True"


class AdminConversationsDeleteschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
