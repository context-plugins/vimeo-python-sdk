from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SelfModel(SdkBaseModel):
    id: str
    name: str


class SelfModelDict(TypedDict):
    id: str
    name: str
