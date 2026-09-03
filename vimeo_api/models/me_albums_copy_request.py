from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MeAlbumsCopyRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """The copied showcase name. By default, this becomes the source showcase name with (Copy) appended."""


class MeAlbumsCopyRequestDict(TypedDict):
    name: NotRequired[str]
