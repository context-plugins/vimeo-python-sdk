from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GridSize(SdkBaseModel):
    """Information about the grid size configuration."""

    is_upgrade: bool
    """Whether an upgrade is required to configure the grid size."""

    value: str
    """The grid size configuration. Possible values include ``s`` for small, ``m`` for medium, ``l`` for large, and
    ``xl`` for extra large."""


class GridSizeDict(TypedDict):
    is_upgrade: bool
    value: str
