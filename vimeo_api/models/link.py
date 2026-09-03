from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .button import Button, ButtonDict
from .picture import Picture, PictureDict
from .secondary_link import SecondaryLink, SecondaryLinkDict


class Link(SdkBaseModel):
    """The links that appear after the video ends."""

    button: Optional[Button] = UNSET
    """The attributes of the button control."""

    description: Optional[str] = UNSET
    """The text that appears beneath the link, if any."""

    name: Optional[str] = UNSET
    """The title of the call to action."""

    picture: OptionalNullable[Picture] = UNSET
    """The background image to display in the area for the call to action."""

    picture_uri: OptionalNullable[str] = UNSET
    """The URI of the background image that appears in the area for the call to action."""

    secondary_link: Optional[SecondaryLink] = UNSET
    """The attributes of the secondary link."""


class LinkDict(TypedDict):
    button: NotRequired[Button | ButtonDict]
    description: NotRequired[str]
    name: NotRequired[str]
    picture: NotRequired[Picture | PictureDict | None]
    picture_uri: NotRequired[str | None]
    secondary_link: NotRequired[SecondaryLink | SecondaryLinkDict]
