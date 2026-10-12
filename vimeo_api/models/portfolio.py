from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.sort1 import Sort1OrStr
from .metadata22 import Metadata22, Metadata22Dict


class Portfolio(SdkBaseModel):
    created_time: str
    """The time in ISO 8601 format when the portfolio was created."""

    description: str | None
    """The description of the portfolio."""

    link: str
    """The link to the portfolio."""

    metadata: Metadata22
    """Metadata about the portfolio."""

    modified_time: str
    """The time in ISO 8601 format when the portfolio's data was last modified."""

    name: str
    """The display name of the portfolio."""

    sort: Sort1OrStr
    """The default video sort order of the portfolio.

    Option descriptions:
     * ``alphabetical`` - The default sort order is alphabetical by name.
     * ``clips`` - The default sort order is video creation date.
     * ``modified`` - The default sort order is the order in which the videos were modified.
     * ``recent`` - The default sort order is the order in which the videos were added."""

    uri: str
    """The canonical relative URI of the portfolio."""


class PortfolioDict(TypedDict):
    created_time: str
    description: str | None
    link: str
    metadata: Metadata22Dict
    modified_time: str
    name: str
    sort: Sort1OrStr
    uri: str
