from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AppsPermissionsRequestschema(SdkBaseModel):
    """Schema for successful response from apps.permissions.request method"""

    ok: Literal["True"] = "True"


class AppsPermissionsRequestschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
