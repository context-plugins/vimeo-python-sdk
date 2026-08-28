from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConversationsClosesuccessschema(SdkBaseModel):
    """Schema for successful response conversations.close method"""

    already_closed: Optional[bool] = UNSET
    no_op: Optional[bool] = UNSET
    ok: Literal["True"] = "True"


class ConversationsClosesuccessschemaDict(TypedDict):
    already_closed: NotRequired[bool]
    no_op: NotRequired[bool]
    ok: NotRequired[Literal["True"]]
