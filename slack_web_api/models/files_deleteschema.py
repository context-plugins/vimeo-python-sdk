from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class FilesDeleteschema(SdkBaseModel):
    """Schema for successful response files.delete method"""

    ok: Literal["True"] = "True"


class FilesDeleteschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
