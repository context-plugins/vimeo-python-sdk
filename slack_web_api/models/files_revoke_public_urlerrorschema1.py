from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.files_revoke_public_urlerror_enum import FilesRevokePublicUrlerrorEnumOrStr


class FilesRevokePublicUrlerrorschema1(SdkBaseModel):
    """Schema for error response from files.revokePublicURL method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: FilesRevokePublicUrlerrorEnumOrStr
    ok: Literal["False"] = "False"


class FilesRevokePublicUrlerrorschema1Dict(TypedDict):
    callstack: NotRequired[str]
    error: FilesRevokePublicUrlerrorEnumOrStr
    ok: NotRequired[Literal["False"]]
