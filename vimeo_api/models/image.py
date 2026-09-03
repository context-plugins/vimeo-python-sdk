from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .picture import Picture, PictureDict


class Image(SdkBaseModel):
    """The custom image that appears after the video ends."""

    description: Optional[str] = UNSET
    """The description of the custom image's content."""

    link: Optional[str] = UNSET
    """The URL that loads upon clicking the custom image."""

    picture: OptionalNullable[Picture] = UNSET
    """The custom image to display."""

    picture_uri: OptionalNullable[str] = UNSET
    """The URI of the custom image to use in the background."""


class ImageDict(TypedDict):
    description: NotRequired[str]
    link: NotRequired[str]
    picture: NotRequired[Picture | PictureDict | None]
    picture_uri: NotRequired[str | None]
