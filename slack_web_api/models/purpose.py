from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Purpose(SdkBaseModel):
    creator: str
    last_set: int
    value: str


class PurposeDict(TypedDict):
    creator: str
    last_set: int
    value: str
