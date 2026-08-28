from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CanThread(SdkBaseModel):
    type_: Optional[list[str]] = Field(default=UNSET, alias="type")
    user: Optional[list[str]] = UNSET


class CanThreadDict(TypedDict):
    type_: NotRequired[list[str]]
    user: NotRequired[list[str]]
