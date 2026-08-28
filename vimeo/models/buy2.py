from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Buy2(SdkBaseModel):
    """Information about purchasing the video."""

    active: bool
    """Whether the video can be purchased."""

    price: Any
    """The purchase price of the video by currency type."""

    purchased: Optional[bool] = UNSET
    """Whether the video has been purchased."""


class Buy2Dict(TypedDict):
    active: bool
    price: Any
    purchased: NotRequired[bool]
