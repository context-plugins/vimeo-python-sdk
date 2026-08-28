from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .reactionobject import Reactionobject, ReactionobjectDict


class FileCommentObject(SdkBaseModel):
    comment: str
    created: int
    id: str
    is_intro: bool
    is_starred: Optional[bool] = UNSET
    num_stars: Optional[int] = UNSET
    pinned_info: Optional[Any] = UNSET
    pinned_to: Optional[list[str]] = UNSET
    reactions: Optional[list[Reactionobject]] = UNSET
    timestamp: int
    user: str


class FileCommentObjectDict(TypedDict):
    comment: str
    created: int
    id: str
    is_intro: bool
    is_starred: NotRequired[bool]
    num_stars: NotRequired[int]
    pinned_info: NotRequired[Any]
    pinned_to: NotRequired[list[str]]
    reactions: NotRequired[list[Reactionobject | ReactionobjectDict]]
    timestamp: int
    user: str
