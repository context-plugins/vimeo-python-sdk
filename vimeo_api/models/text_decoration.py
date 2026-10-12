from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .assets import Assets, AssetsDict
from .enums.type12 import Type12OrStr


class TextDecoration(SdkBaseModel):
    assets: Optional[Assets] = UNSET
    """The assets that are needed to decorate the text."""

    text: str
    """The note text to decorate."""

    type_: Type12OrStr = Field(alias="type")
    """The type of text decoration.

    Option descriptions:
     * ``url`` - The URL of the Vimeo video."""


class TextDecorationDict(TypedDict):
    assets: NotRequired[AssetsDict]
    text: str
    type_: Type12OrStr
