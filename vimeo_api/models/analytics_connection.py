from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .analytics import Analytics, AnalyticsDict
from .paging import Paging, PagingDict


class AnalyticsConnection(SdkBaseModel):
    total: Optional[int] = UNSET
    page: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    paging: Optional[Paging] = UNSET
    data: Optional[list[Analytics]] = UNSET


class AnalyticsConnectionDict(TypedDict):
    total: NotRequired[int]
    page: NotRequired[int]
    per_page: NotRequired[int]
    paging: NotRequired[PagingDict]
    data: NotRequired[list[AnalyticsDict]]
