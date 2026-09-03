from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filters import Filters, FiltersDict


class ChildTextTracks(SdkBaseModel):
    """Metadata for the child text tracks. This data requires a bearer token with the ``private`` scope."""

    filters: Optional[Filters] = UNSET
    """The request filters to use for child text tracks. This data requires a bearer token with the ``private``
    scope."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class ChildTextTracksDict(TypedDict):
    filters: NotRequired[Filters | FiltersDict]
    options: NotRequired[list[str]]
    uri: NotRequired[str]
