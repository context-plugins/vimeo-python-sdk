from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .disabled2 import Disabled2, Disabled2Dict


class AvailableAlbums(SdkBaseModel):
    """Information about the available showcases, or the showcases to which the video can be added. This data requires a
    bearer token with the ``private`` scope."""

    disabled: Optional[Disabled2] = UNSET
    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    total: Optional[float] = UNSET
    """The total number of showcases on this connection. This data requires a bearer token with the ``private``
    scope."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class AvailableAlbumsDict(TypedDict):
    disabled: NotRequired[Disabled2Dict]
    options: NotRequired[list[str]]
    total: NotRequired[float]
    uri: NotRequired[str]
