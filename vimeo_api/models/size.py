from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Size(SdkBaseModel):
    height: float
    """The height of the picture in pixels."""

    link: str
    """The direct link to the image file. For information about the format of the image file, see our `Working with
    Thumbnail Uploads <https://developer.vimeo.com/api/upload/thumbnails#returning-the-link-to-a-thumbnail>`__ guide."""

    link_with_play_button: Optional[str] = UNSET
    """The direct link to the image file with a play button overlay. For information about the format of the image file,
    see our `Working with Thumbnail Uploads
    <https://developer.vimeo.com/api/upload/thumbnails#returning-the-link-to-a-thumbnail>`__ guide."""

    width: float
    """The width of the picture in pixels."""


class SizeDict(TypedDict):
    height: float
    link: str
    link_with_play_button: NotRequired[str]
    width: float
