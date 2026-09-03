from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type36 import Type36OrStr


class EndScreen4(SdkBaseModel):
    type_: Optional[Type36OrStr] = Field(default=UNSET, alias="type")
    """The end screen type.

    Option descriptions:
     * ``empty`` - The end screen is empty.
     * ``loop`` - The end screen loops the video playback.
     * ``share`` - The end screen includes sharing options.
     * ``thumbnail`` - The end screen includes the thumbnail of the video."""


class EndScreen4Dict(TypedDict):
    type_: NotRequired[Type36OrStr]
