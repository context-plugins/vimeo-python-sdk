from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LiveEventsComposerScenesGraphicsRequest(SdkBaseModel):
    item: Any
    """The content of the graphic item."""


class LiveEventsComposerScenesGraphicsRequestDict(TypedDict):
    item: Any
