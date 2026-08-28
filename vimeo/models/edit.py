from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Edit(SdkBaseModel):
    """Information about where and how to edit a video."""

    blocked_fields: list[str]
    """An array of video fields that a user can't interact with."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class EditDict(TypedDict):
    blocked_fields: list[str]
    options: list[str]
    uri: str
