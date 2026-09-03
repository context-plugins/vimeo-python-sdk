from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type5 import Type5OrStr


class SentimentWidget(SdkBaseModel):
    end_time: float
    """The playback position in seconds when the widget disappears."""

    headline: str
    """The headline text shown above the widget."""

    id: str
    """The unique identifier of the sentiment widget."""

    start_time: float
    """The playback position in seconds when the widget appears."""

    type_: Type5OrStr = Field(alias="type")
    """The widget variant: ``thumbs`` or ``ranking``.

    Option descriptions:
     * ``ranking`` - The widget shows a ranking of options.
     * ``thumbs`` - The widget shows thumbs up/down buttons."""


class SentimentWidgetDict(TypedDict):
    end_time: float
    headline: str
    id: str
    start_time: float
    type_: Type5OrStr
