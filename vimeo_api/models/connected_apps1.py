from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConnectedApps1(SdkBaseModel):
    all_scopes: Optional[Any] = UNSET
    """The list of all the scopes on the connected app that are needed for a particular Vimeo feature."""

    is_connected: Optional[bool] = UNSET
    """Whether the authenticated user is connected to the connected app."""

    needed_scopes: Optional[Any] = UNSET
    """The list of the remaining scopes on the connected app that the authenticated user needs for a particular Vimeo
    feature."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    uri: Optional[str] = UNSET
    """The URI of the connected app."""


class ConnectedApps1Dict(TypedDict):
    all_scopes: NotRequired[Any]
    is_connected: NotRequired[bool]
    needed_scopes: NotRequired[Any]
    options: NotRequired[list[str]]
    uri: NotRequired[str]
