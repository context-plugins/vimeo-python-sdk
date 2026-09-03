from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type34 import Type34OrStr


class EndScreen2(SdkBaseModel):
    type_: Optional[Type34OrStr] = Field(default=UNSET, alias="type")
    """The end screen type.

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


class EndScreen2Dict(TypedDict):
    type_: NotRequired[Type34OrStr]
