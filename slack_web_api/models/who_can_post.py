from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WhoCanPost(SdkBaseModel):
    type_: Optional[list[str]] = Field(default=UNSET, alias="type")
    user: Optional[list[str]] = UNSET


class WhoCanPostDict(TypedDict):
    type_: NotRequired[list[str]]
    user: NotRequired[list[str]]
