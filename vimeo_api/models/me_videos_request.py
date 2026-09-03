from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MeVideosRequest(SdkBaseModel):
    send_to_recently_deleted: Optional[bool] = UNSET
    """When true, deleted videos use the Recently Deleted purgatory bucket (30-day retention)."""


class MeVideosRequestDict(TypedDict):
    send_to_recently_deleted: NotRequired[bool]
