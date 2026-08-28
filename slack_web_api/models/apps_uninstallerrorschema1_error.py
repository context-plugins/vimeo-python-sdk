from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.apps_uninstall_error_enum import AppsUninstallErrorEnumOrStr


class AppsUninstallerrorschema1Error(SdkBaseModel):
    """Schema for error response from apps.uninstall method"""

    callstack: Optional[str] = UNSET
    """Note: PHP callstack is only visible in dev/qa"""

    error: AppsUninstallErrorEnumOrStr
    ok: Literal["False"] = "False"


class AppsUninstallerrorschema1ErrorDict(TypedDict):
    callstack: NotRequired[str]
    error: AppsUninstallErrorEnumOrStr
    ok: NotRequired[Literal["False"]]
