from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Season(SdkBaseModel):
    """Information about the video's season."""

    name: Optional[str] = UNSET
    """The name of the season."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data."""


class SeasonDict(TypedDict):
    name: NotRequired[str]
    options: NotRequired[list[str]]
    uri: NotRequired[str]
