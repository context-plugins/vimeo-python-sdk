from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MeProjectsVideosRequest(SdkBaseModel):
    send_to_recently_deleted: Optional[bool] = UNSET
    """When deleting clips, use Recently Deleted purgatory when true."""

    should_delete_clips: Optional[bool] = UNSET
    """Whether to delete the videos when removing them from the folder."""

    uris: str
    """A comma-separated list of the video URIs to remove."""


class MeProjectsVideosRequestDict(TypedDict):
    send_to_recently_deleted: NotRequired[bool]
    should_delete_clips: NotRequired[bool]
    uris: str
