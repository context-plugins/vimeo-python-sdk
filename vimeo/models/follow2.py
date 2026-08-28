from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Follow2(SdkBaseModel):
    """Information about the followed status of the authenticated user."""

    added: Optional[bool] = UNSET
    """Whether the authenticated user is following the requested user."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    uri: Optional[str] = UNSET
    """The URI to follow the requested user."""


class Follow2Dict(TypedDict):
    added: NotRequired[bool]
    options: NotRequired[list[str]]
    uri: NotRequired[str]
