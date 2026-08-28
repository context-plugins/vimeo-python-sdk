from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AdminConversationsConvertToPrivateschema(SdkBaseModel):
    """Schema for successful response of admin.conversations.convertToPrivate"""

    ok: Literal["True"] = "True"


class AdminConversationsConvertToPrivateschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
