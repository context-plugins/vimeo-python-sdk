from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .content_rating import ContentRating, ContentRatingDict
from .paging import Paging, PagingDict


class ContentRatingConnection(SdkBaseModel):
    total: Optional[int] = UNSET
    page: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    paging: Optional[Paging] = UNSET
    data: Optional[list[ContentRating]] = UNSET


class ContentRatingConnectionDict(TypedDict):
    total: NotRequired[int]
    page: NotRequired[int]
    per_page: NotRequired[int]
    paging: NotRequired[PagingDict]
    data: NotRequired[list[ContentRatingDict]]
