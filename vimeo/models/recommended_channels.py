from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RecommendedChannels(SdkBaseModel):
    """A collection of recommended channels for the authenticated user to follow. This data requires a bearer token with
    the ``private`` scope. This data requires a bearer token with the ``private`` scope."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    total: Optional[float] = UNSET
    """The total number of channels on this connection. This data requires a bearer token with the ``private`` scope."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class RecommendedChannelsDict(TypedDict):
    options: NotRequired[list[str]]
    total: NotRequired[float]
    uri: NotRequired[str]
