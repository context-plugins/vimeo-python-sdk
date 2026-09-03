from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ParentTextTrack(SdkBaseModel):
    """Metadata for the parent text track."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data."""


class ParentTextTrackDict(TypedDict):
    options: NotRequired[list[str]]
    uri: NotRequired[str]
