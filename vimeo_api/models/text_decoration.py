from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .assets import Assets, AssetsDict


class TextDecoration(SdkBaseModel):
    assets: Optional[Assets] = UNSET
    """The assets that are needed to decorate the text."""

    text: str
    """The note text to decorate."""

    type_: Literal["url"] = Field(default="url", alias="type")
    """The type of text decoration.

    Option descriptions:
     * ``url`` - The URL of the Vimeo video."""


class TextDecorationDict(TypedDict):
    assets: NotRequired[Assets | AssetsDict]
    text: str
    type_: NotRequired[Literal["url"]]
