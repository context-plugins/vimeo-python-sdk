from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersLiveEventsPicturesThumbnailIdRequest(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether the thumbnail is the event's active thumbnail."""


class UsersLiveEventsPicturesThumbnailIdRequestDict(TypedDict):
    active: NotRequired[bool]
