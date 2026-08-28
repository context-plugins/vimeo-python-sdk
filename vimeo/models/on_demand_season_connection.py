from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .on_demand_season import OnDemandSeason, OnDemandSeasonDict
from .paging import Paging, PagingDict


class OnDemandSeasonConnection(SdkBaseModel):
    total: Optional[int] = UNSET
    page: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    paging: Optional[Paging] = UNSET
    data: Optional[list[OnDemandSeason]] = UNSET


class OnDemandSeasonConnectionDict(TypedDict):
    total: NotRequired[int]
    page: NotRequired[int]
    per_page: NotRequired[int]
    paging: NotRequired[Paging | PagingDict]
    data: NotRequired[list[OnDemandSeason | OnDemandSeasonDict]]
