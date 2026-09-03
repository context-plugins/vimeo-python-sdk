from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LegalHold(SdkBaseModel):
    """The associated legal hold object."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class LegalHoldDict(TypedDict):
    options: list[str]
    uri: str
