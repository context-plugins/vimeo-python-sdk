from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.files_upload_error_enum import FilesUploadErrorEnumOrStr


class FilesUploaderrorschema1(SdkBaseModel):
    """Schema for error response files.upload method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: FilesUploadErrorEnumOrStr
    ok: Literal["False"] = "False"


class FilesUploaderrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: FilesUploadErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
