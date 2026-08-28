from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConversationsOpensuccessschema(SdkBaseModel):
    """Schema for successful response from conversations.open method when opening channels, ims, mpims"""

    already_open: Optional[bool] = UNSET
    channel: Any
    no_op: Optional[bool] = UNSET
    ok: Literal["True"] = "True"


class ConversationsOpensuccessschemaDict(TypedDict):
    already_open: NotRequired[bool]
    channel: Any
    no_op: NotRequired[bool]
    ok: NotRequired[Literal["True"]]
