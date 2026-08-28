from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .info import Info, InfoDict


class AppsPermissionsInfoschema(SdkBaseModel):
    """Schema for successful response from apps.permissions.info method"""

    info: Info
    ok: Literal["True"] = "True"


class AppsPermissionsInfoschemaDict(TypedDict):
    info: Info | InfoDict
    ok: NotRequired[Literal["True"]]
