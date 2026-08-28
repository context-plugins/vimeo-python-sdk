from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ConversationsArchivesuccessschema(SdkBaseModel):
    """Schema for successful response conversations.archive method"""

    ok: Literal["True"] = "True"


class ConversationsArchivesuccessschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
