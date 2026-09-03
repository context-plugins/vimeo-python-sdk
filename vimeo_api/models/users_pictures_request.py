from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersPicturesRequest(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether the picture is the authenticated user's active portrait."""


class UsersPicturesRequestDict(TypedDict):
    active: NotRequired[bool]
