from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type25 import Type25OrStr
from .image import Image, ImageDict
from .link import Link, LinkDict
from .share import Share, ShareDict
from .text import Text, TextDict
from .videos15 import Videos15, Videos15Dict


class EndScreen1(SdkBaseModel):
    """A representation of the end screen settings."""

    image: Optional[Image] = UNSET
    """The custom image that appears after the video ends."""

    link: Optional[Link] = UNSET
    """The links that appear after the video ends."""

    share: Optional[Share] = UNSET
    """The share options that appear after the video ends."""

    text: Optional[Text] = UNSET
    """The text block that appears after the video ends."""

    type_: Type25OrStr = Field(alias="type")
    """The elements that appear after the video ends.

    Option descriptions:
     * ``beginning`` - The end screen is a thumbnail.
     * ``custom`` - The end screen is custom.
     * ``email`` - The end screen is an email form.
     * ``image`` - The end screen is an image.
     * ``link`` - The end screen is a link.
     * ``loop`` - The end screen is a loop.
     * ``nothing`` - There is no end screen.
     * ``share`` - The end screen is a share button.
     * ``text`` - The end screen is text.
     * ``threevideos`` - The end screen is three video suggestions.
     * ``videos`` - The end screen is video suggestions."""

    videos: Optional[Videos15] = UNSET
    """The additional videos that are offered after the main video ends."""


class EndScreen1Dict(TypedDict):
    image: NotRequired[Image | ImageDict]
    link: NotRequired[Link | LinkDict]
    share: NotRequired[Share | ShareDict]
    text: NotRequired[Text | TextDict]
    type_: Type25OrStr
    videos: NotRequired[Videos15 | Videos15Dict]
