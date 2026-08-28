from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class FilesCommentsDeleteschema(SdkBaseModel):
    """Schema for successful response files.comments.delete method"""

    ok: Literal["True"] = "True"


class FilesCommentsDeleteschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
