from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AddSubfolder(SdkBaseModel):
    """Information about adding a subfolder to the current folder."""

    can_add_subfolders: bool
    """Whether the folder can contain a subfolder."""

    content_type: Optional[str] = UNSET
    """The subfolder content type."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    properties: Optional[list[str]] = UNSET
    """Properties that can be added to the request body."""

    subfolder_depth_limit_reached: bool
    """Whether the user has reached the maximum subfolder depth."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data."""


class AddSubfolderDict(TypedDict):
    can_add_subfolders: bool
    content_type: NotRequired[str]
    options: NotRequired[list[str]]
    properties: NotRequired[list[str]]
    subfolder_depth_limit_reached: bool
    uri: NotRequired[str]
