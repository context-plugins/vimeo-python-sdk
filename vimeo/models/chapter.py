from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .picture import Picture, PictureDict


class Chapter(SdkBaseModel):
    active_thumbnail_uri: Optional[str] = UNSET
    """The URI of the active thumbnail."""

    thumbnails: list[Picture]
    """The thumbnails associated with the video chapter."""

    timecode: float
    """The timecode of the chapter in seconds from the start of the video."""

    title: str
    """The title of the chapter."""

    uri: str
    """The relative URI of the chapter."""


class ChapterDict(TypedDict):
    active_thumbnail_uri: NotRequired[str]
    thumbnails: list[Picture | PictureDict]
    timecode: float
    title: str
    uri: str
