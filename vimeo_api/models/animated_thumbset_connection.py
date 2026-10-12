from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .animated_thumbset import AnimatedThumbset, AnimatedThumbsetDict
from .paging import Paging, PagingDict


class AnimatedThumbsetConnection(SdkBaseModel):
    total: Optional[int] = UNSET
    page: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    paging: Optional[Paging] = UNSET
    data: Optional[list[AnimatedThumbset]] = UNSET


class AnimatedThumbsetConnectionDict(TypedDict):
    total: NotRequired[int]
    page: NotRequired[int]
    per_page: NotRequired[int]
    paging: NotRequired[PagingDict]
    data: NotRequired[list[AnimatedThumbsetDict]]
