from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .fileobject import Fileobject, FileobjectDict
from .pagingobject import Pagingobject, PagingobjectDict


class FilesInfoschema(SdkBaseModel):
    """Schema for successful response from files.info method"""

    comments: list[Any]
    content_html: OptionalNullable[str] = UNSET
    editor: Optional[str] = UNSET
    file: Fileobject
    ok: Literal["True"] = "True"
    paging: Optional[Pagingobject] = UNSET
    response_metadata: Optional[Any] = UNSET


class FilesInfoschemaDict(TypedDict):
    comments: list[Any]
    content_html: NotRequired[str | None]
    editor: NotRequired[str]
    file: Fileobject | FileobjectDict
    ok: NotRequired[Literal["True"]]
    paging: NotRequired[Pagingobject | PagingobjectDict]
    response_metadata: NotRequired[Any]
