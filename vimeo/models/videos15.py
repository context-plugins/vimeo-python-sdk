from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.outro_videos_collection_type import OutroVideosCollectionTypeOrStr
from .picture import Picture, PictureDict


class Videos15(SdkBaseModel):
    """The additional videos that are offered after the main video ends."""

    outro_videos_collection_type: OptionalNullable[OutroVideosCollectionTypeOrStr] = UNSET
    """The source of the video collection that appears in the area for more videos.

    Option descriptions:
     * ``album`` - The video collection source is a user showcase.
     * ``all_videos`` - The video collection source is all user videos.
     * ``channel`` - The video collection source is a user channel.
     * ``group`` - The video collection source is a user group.
     * ``likes`` - The video collection source is user likes.
     * ``uploaded_videos`` - The video collection source is user uploads."""

    outro_videos_collection_uri: OptionalNullable[str] = UNSET
    """The URI of the video collection that appears in the area for more videos when the value of
    **videos.outro_videos_collection_type** is ``album``."""

    picture: OptionalNullable[Picture] = UNSET
    """The background image to display in the area for more videos."""

    picture_uri: OptionalNullable[str] = UNSET
    """The URI of the background image that appears in the area for more videos."""

    video_uris: Optional[list[str]] = UNSET
    """The URIs of the videos when the value of **videos.outro_videos_collection_type** is ``uploaded_videos``."""


class Videos15Dict(TypedDict):
    outro_videos_collection_type: NotRequired[OutroVideosCollectionTypeOrStr | None]
    outro_videos_collection_uri: NotRequired[str | None]
    picture: NotRequired[Picture | PictureDict | None]
    picture_uri: NotRequired[str | None]
    video_uris: NotRequired[list[str]]
