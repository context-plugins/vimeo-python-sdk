from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Paging(SdkBaseModel):
    next: OptionalNullable[str] = UNSET
    previous: OptionalNullable[str] = UNSET
    first: OptionalNullable[str] = UNSET
    last: OptionalNullable[str] = UNSET


class PagingDict(TypedDict):
    next: NotRequired[str | None]
    previous: NotRequired[str | None]
    first: NotRequired[str | None]
    last: NotRequired[str | None]
