from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Block1(SdkBaseModel):
    """Information about the block status of the authenticated user."""

    added: bool
    """Whether the authenticated user is blocking the requested user."""

    added_time: Optional[str] = UNSET
    """The time in ISO 8601 format when the block occurred, or the null value if no block exists."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The URI to block or unblock the requested user."""


class Block1Dict(TypedDict):
    added: bool
    added_time: NotRequired[str]
    options: list[str]
    uri: str
