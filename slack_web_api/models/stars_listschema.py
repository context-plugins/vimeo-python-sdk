from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagingobject import Pagingobject, PagingobjectDict


class StarsListschema(SdkBaseModel):
    """Schema for successful response from stars.list method"""

    items: list[Any]
    ok: Literal["True"] = "True"
    paging: Optional[Pagingobject] = UNSET


class StarsListschemaDict(TypedDict):
    items: list[Any]
    ok: NotRequired[Literal["True"]]
    paging: NotRequired[Pagingobject | PagingobjectDict]
