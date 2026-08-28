from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MeVideosCopyRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """The copied video name. By default, this becomes the source video name with (Copy) appended."""


class MeVideosCopyRequestDict(TypedDict):
    name: NotRequired[str]
