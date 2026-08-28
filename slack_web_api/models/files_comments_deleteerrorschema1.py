from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.files_comments_delete_error_enum import FilesCommentsDeleteErrorEnumOrStr


class FilesCommentsDeleteerrorschema1(SdkBaseModel):
    """Schema for error response files.comments.delete method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: FilesCommentsDeleteErrorEnumOrStr
    ok: Literal["False"] = "False"


class FilesCommentsDeleteerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: FilesCommentsDeleteErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
