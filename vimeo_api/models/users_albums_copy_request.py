from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersAlbumsCopyRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """The copied showcase name. By default, this becomes the source showcase name with (Copy) appended."""


class UsersAlbumsCopyRequestDict(TypedDict):
    name: NotRequired[str]
