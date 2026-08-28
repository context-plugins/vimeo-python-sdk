from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .fileobject import Fileobject, FileobjectDict
from .pagingobject import Pagingobject, PagingobjectDict


class FilesListschema(SdkBaseModel):
    """Schema for successful response from files.list method"""

    files: list[Fileobject]
    ok: Literal["True"] = "True"
    paging: Pagingobject


class FilesListschemaDict(TypedDict):
    files: list[Fileobject | FileobjectDict]
    ok: NotRequired[Literal["True"]]
    paging: Pagingobject | PagingobjectDict
