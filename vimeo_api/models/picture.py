from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type import TypeOrStr
from .size import Size, SizeDict


class Picture(SdkBaseModel):
    active: bool
    """Whether the picture is currently active."""

    base_link: str
    """The base link to the image file, without any parameters."""

    default_picture: bool
    """Whether the picture is Vimeo's default."""

    link: Optional[str] = UNSET
    """The upload URL of the picture. This field appears upon the initial creation of a picture resource."""

    resource_key: str
    """The resource key string of the picture."""

    sizes: list[Size]
    """An array containing reference information about all available image files."""

    type_: TypeOrStr = Field(alias="type")
    """The type of picture.

    Option descriptions:
     * ``caution`` - The picture isn't appropriate for all ages.
     * ``custom`` - The picture is a custom video image.
     * ``default`` - The picture is the default video image."""

    uri: str
    """The URI of the picture."""


class PictureDict(TypedDict):
    active: bool
    base_link: str
    default_picture: bool
    link: NotRequired[str]
    resource_key: str
    sizes: list[SizeDict]
    type_: TypeOrStr
    uri: str
