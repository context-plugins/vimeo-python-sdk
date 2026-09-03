from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Text(SdkBaseModel):
    """The text block that appears after the video ends."""

    description: Optional[str] = UNSET
    """The text of the description."""


class TextDict(TypedDict):
    description: NotRequired[str]
