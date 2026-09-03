from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .paging import Paging, PagingDict
from .portfolio import Portfolio, PortfolioDict


class PortfolioConnection(SdkBaseModel):
    total: Optional[int] = UNSET
    page: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    paging: Optional[Paging] = UNSET
    data: Optional[list[Portfolio]] = UNSET


class PortfolioConnectionDict(TypedDict):
    total: NotRequired[int]
    page: NotRequired[int]
    per_page: NotRequired[int]
    paging: NotRequired[Paging | PagingDict]
    data: NotRequired[list[Portfolio | PortfolioDict]]
