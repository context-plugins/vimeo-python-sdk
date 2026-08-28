from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.files_info_error_enum import FilesInfoErrorEnumOrStr


class FilesInfoerrorschema1(SdkBaseModel):
    """Schema for error response from files.info method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: FilesInfoErrorEnumOrStr
    ok: Literal["False"] = "False"


class FilesInfoerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: FilesInfoErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
