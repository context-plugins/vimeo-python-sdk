from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ObjsPrimaryOwner(SdkBaseModel):
    email: str
    id: str


class ObjsPrimaryOwnerDict(TypedDict):
    email: str
    id: str
