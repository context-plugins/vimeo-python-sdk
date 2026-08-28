from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ConversationsMarksuccessschema(SdkBaseModel):
    """Schema for successful response conversations.mark method"""

    ok: Literal["True"] = "True"


class ConversationsMarksuccessschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
