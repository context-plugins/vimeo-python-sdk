from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ConversationsUnarchivesuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.unarchive method"""

    ok: Literal["True"] = "True"


class ConversationsUnarchivesuccessschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
