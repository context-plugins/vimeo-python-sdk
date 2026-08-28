from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Reactionobject(SdkBaseModel):
    count: int
    name: str
    users: list[str]


class ReactionobjectDict(TypedDict):
    count: int
    name: str
    users: list[str]
