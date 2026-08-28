from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.files_delete_error_enum import FilesDeleteErrorEnumOrStr


class FilesDeleteerrorschema1Error(SdkBaseModel):
    """Schema for error response files.delete method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: FilesDeleteErrorEnumOrStr
    ok: Literal["False"] = "False"


class FilesDeleteerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: FilesDeleteErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
