from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersAlbumsCustomThumbnailsThumbnailIdRequest(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether to make this image the active custom showcase thumbnail."""


class UsersAlbumsCustomThumbnailsThumbnailIdRequestDict(TypedDict):
    active: NotRequired[bool]
