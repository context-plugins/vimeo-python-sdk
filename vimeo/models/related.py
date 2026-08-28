from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Related(SdkBaseModel):
    """Information about the video's related content."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data."""


class RelatedDict(TypedDict):
    options: NotRequired[list[str]]
    uri: NotRequired[str]
