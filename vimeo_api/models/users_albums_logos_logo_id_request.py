from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersAlbumsLogosLogoIdRequest(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether to make this image the active showcase logo."""


class UsersAlbumsLogosLogoIdRequestDict(TypedDict):
    active: NotRequired[bool]
