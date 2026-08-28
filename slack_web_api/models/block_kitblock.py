from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BlockKitblock(SdkBaseModel):
    type_: str = Field(alias="type")


class BlockKitblockDict(TypedDict):
    type_: str
