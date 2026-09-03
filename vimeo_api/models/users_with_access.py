from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersWithAccess(SdkBaseModel):
    """Information about the user privacy of the video, if the video privacy setting is ``users``."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    total: Optional[float] = UNSET
    """The total number of users on this connection."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data."""


class UsersWithAccessDict(TypedDict):
    options: NotRequired[list[str]]
    total: NotRequired[float]
    uri: NotRequired[str]
