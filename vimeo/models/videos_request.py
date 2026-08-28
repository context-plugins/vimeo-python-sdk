from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosRequest(SdkBaseModel):
    send_to_recently_deleted: Optional[bool] = UNSET
    """When true, the video is placed in the Recently Deleted purgatory bucket (30-day retention). When false or
    omitted, legacy user-delete purgatory applies."""


class VideosRequestDict(TypedDict):
    send_to_recently_deleted: NotRequired[bool]
