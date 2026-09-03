from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowSearchBar(SdkBaseModel):
    """Information about showing the search bar in the featured content layout."""

    is_upgrade: bool
    """Whether an upgrade is required to show the search bar in the featured content layout."""

    value: bool
    """Whether to show the search bar in the featured content layout."""


class ShowSearchBarDict(TypedDict):
    is_upgrade: bool
    value: bool
