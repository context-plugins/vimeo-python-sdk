from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ComposerGraphics(SdkBaseModel):
    created_at: float = Field(alias="createdAt")
    """The timestamp in milliseconds since the Unix epoch when the item was created."""

    id: str
    """The unique identifier of the graphic item."""

    type_: str = Field(alias="type")
    """The type of the graphic item. The value of this field is always ``agoraMedia`` for this object."""

    updated_at: float = Field(alias="updatedAt")
    """The timestamp in milliseconds since the Unix epoch when the item was last updated."""

    video_duration: float = Field(alias="videoDuration")
    """The length of the video in seconds."""

    video_id: float = Field(alias="videoId")
    """The unique identifier of the video resource."""

    video_thumb: str = Field(alias="videoThumb")
    """The URL to the standard-resolution video thumbnail image."""

    video_thumb_full_size: str = Field(alias="videoThumbFullSize")
    """The URL to the high-resolution video thumbnail image."""


class ComposerGraphicsDict(TypedDict):
    created_at: float
    id: str
    type_: str
    updated_at: float
    video_duration: float
    video_id: float
    video_thumb: str
    video_thumb_full_size: str
