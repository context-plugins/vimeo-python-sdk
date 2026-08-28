from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Messageobject1(SdkBaseModel):
    attachments: Optional[list[Any]] = UNSET
    blocks: Optional[Any] = UNSET
    text: str


class Messageobject1Dict(TypedDict):
    attachments: NotRequired[list[Any]]
    blocks: NotRequired[Any]
    text: str
