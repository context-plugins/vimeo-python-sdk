from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .show_search_bar import ShowSearchBar, ShowSearchBarDict


class NavigationConfig(SdkBaseModel):
    show_search_bar: ShowSearchBar
    """Information about showing the search bar in the featured content layout."""


class NavigationConfigDict(TypedDict):
    show_search_bar: ShowSearchBarDict
