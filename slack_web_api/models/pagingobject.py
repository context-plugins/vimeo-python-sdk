from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Pagingobject(SdkBaseModel):
    count: Optional[int] = UNSET
    page: int
    pages: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    spill: Optional[int] = UNSET
    total: int


class PagingobjectDict(TypedDict):
    count: NotRequired[int]
    page: int
    pages: NotRequired[int]
    per_page: NotRequired[int]
    spill: NotRequired[int]
    total: int
