from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Validate(SdkBaseModel):
    """Information about where and how to validate a video field."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The URI that resolves to the connection data."""


class ValidateDict(TypedDict):
    options: list[str]
    uri: str
