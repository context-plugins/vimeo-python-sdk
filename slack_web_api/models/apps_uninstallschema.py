from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AppsUninstallschema(SdkBaseModel):
    """Schema for successful response from apps.uninstall method"""

    ok: Literal["True"] = "True"


class AppsUninstallschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
