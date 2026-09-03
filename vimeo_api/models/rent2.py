from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Rent2(SdkBaseModel):
    """Information about renting the video."""

    active: bool
    """Whether the video can be rented."""

    price: Any
    """The rental price of the video by currency type."""

    purchased: Optional[bool] = UNSET
    """Whether the video has been rented."""


class Rent2Dict(TypedDict):
    active: bool
    price: Any
    purchased: NotRequired[bool]
