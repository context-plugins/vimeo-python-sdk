from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type4 import Type4OrStr


class EndScreen(SdkBaseModel):
    type_: Type4OrStr = Field(alias="type")
    """How the embeddable player handles the end screen.

    Option descriptions:
     * ``empty`` - The end screen is empty.
     * ``loop`` - The end screen loops the video playback.
     * ``share`` - The end screen includes sharing options.
     * ``thumbnail`` - The end screen includes the thumbnail of the video."""


class EndScreenDict(TypedDict):
    type_: Type4OrStr
