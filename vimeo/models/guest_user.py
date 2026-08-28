from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GuestUser(SdkBaseModel):
    """Information about the guest user who posted the comment."""

    name: str
    """The display name of the guest user who posted the comment."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The unique identifier to access the guest user resource."""


class GuestUserDict(TypedDict):
    name: str
    options: NotRequired[list[str]]
    uri: str
