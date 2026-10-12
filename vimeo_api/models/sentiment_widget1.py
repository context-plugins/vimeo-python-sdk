from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type54 import Type54OrStr


class SentimentWidget1(SdkBaseModel):
    end_time: Optional[float] = UNSET
    """The playback position in seconds when the widget disappears."""

    headline: Optional[str] = UNSET
    """The headline text shown above the widget."""

    id: Optional[str] = UNSET
    """The unique identifier of the sentiment widget."""

    start_time: Optional[float] = UNSET
    """The playback position in seconds when the widget appears."""

    type_: Optional[Type54OrStr] = Field(default=UNSET, alias="type")
    """The widget variant.

    Option descriptions:
     * ``ranking`` - The widget shows a ranking of options.
     * ``thumbs`` - The widget shows thumbs up/down buttons."""


class SentimentWidget1Dict(TypedDict):
    end_time: NotRequired[float]
    headline: NotRequired[str]
    id: NotRequired[str]
    start_time: NotRequired[float]
    type_: NotRequired[Type54OrStr]
