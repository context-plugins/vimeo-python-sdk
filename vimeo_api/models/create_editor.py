from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateEditor(SdkBaseModel):
    """Information about where and how to edit a video using the Vimeo Create editor."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The URI that resolves to the connection data."""


class CreateEditorDict(TypedDict):
    options: list[str]
    uri: str
