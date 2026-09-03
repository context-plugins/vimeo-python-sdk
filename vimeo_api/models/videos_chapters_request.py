from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class VideosChaptersRequest(SdkBaseModel):
    active_thumbnail_uri: Optional[str] = UNSET
    """The URI of the chapter's active thumbnail."""

    thumbnail_uris: Optional[list[str]] = UNSET
    """An array of URIs of the thumbnails associated with the video chapter."""

    timecode: OptionalNullable[float] = UNSET
    """The timecode of the chapter in seconds from the start of the video."""

    title: OptionalNullable[str] = UNSET
    """The title of the chapter."""


class VideosChaptersRequestDict(TypedDict):
    active_thumbnail_uri: NotRequired[str]
    thumbnail_uris: NotRequired[list[str]]
    timecode: NotRequired[float | None]
    title: NotRequired[str | None]
