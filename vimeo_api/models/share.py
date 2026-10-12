from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .picture import Picture, PictureDict


class Share(SdkBaseModel):
    """The share options that appear after the video ends."""

    picture: OptionalNullable[Picture] = UNSET
    """The image to display behind the share options."""

    picture_uri: OptionalNullable[str] = UNSET
    """The URI of the background image that appears behind the share options."""


class ShareDict(TypedDict):
    picture: NotRequired[PictureDict | None]
    picture_uri: NotRequired[str | None]
