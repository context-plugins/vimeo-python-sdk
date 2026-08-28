from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .fileobject import Fileobject, FileobjectDict


class FilesUploadschema(SdkBaseModel):
    """Schema for successful response files.upload method"""

    file: Fileobject
    ok: Literal["True"] = "True"


class FilesUploadschemaDict(TypedDict):
    file: Fileobject | FileobjectDict
    ok: NotRequired[Literal["True"]]
