from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Topic(SdkBaseModel):
    creator: str
    last_set: int
    value: str


class TopicDict(TypedDict):
    creator: str
    last_set: int
    value: str
