from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .on_demand_page import OnDemandPage, OnDemandPageDict
from .paging import Paging, PagingDict


class OnDemandPageConnection(SdkBaseModel):
    total: Optional[int] = UNSET
    page: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    paging: Optional[Paging] = UNSET
    data: Optional[list[OnDemandPage]] = UNSET


class OnDemandPageConnectionDict(TypedDict):
    total: NotRequired[int]
    page: NotRequired[int]
    per_page: NotRequired[int]
    paging: NotRequired[PagingDict]
    data: NotRequired[list[OnDemandPageDict]]
