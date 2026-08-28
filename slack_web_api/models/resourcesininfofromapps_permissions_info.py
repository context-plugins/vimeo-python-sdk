from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResourcesininfofromappsPermissionsInfo(SdkBaseModel):
    excluded_ids: Optional[list[Any]] = UNSET
    ids: list[Any]
    wildcard: Optional[bool] = UNSET


class ResourcesininfofromappsPermissionsInfoDict(TypedDict):
    excluded_ids: NotRequired[list[Any]]
    ids: list[Any]
    wildcard: NotRequired[bool]
