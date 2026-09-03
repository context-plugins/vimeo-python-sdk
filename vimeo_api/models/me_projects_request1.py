from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MeProjectsRequest1(SdkBaseModel):
    send_to_recently_deleted: Optional[bool] = UNSET
    """When true and should_delete_clips is true, deleted videos use the Recently Deleted purgatory bucket (30-day
    retention)."""

    should_delete_clips: Optional[bool] = UNSET
    """Whether to delete all the videos in the folder along with the folder itself."""


class MeProjectsRequest1Dict(TypedDict):
    send_to_recently_deleted: NotRequired[bool]
    should_delete_clips: NotRequired[bool]
