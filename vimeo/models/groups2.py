from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Groups2(SdkBaseModel):
    """A standard connection object indicating how to return groups that this team user is a part of."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Groups2Dict(TypedDict):
    options: list[str]
    uri: str
