from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AddPrivacyUser(SdkBaseModel):
    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class AddPrivacyUserDict(TypedDict):
    options: NotRequired[list[str]]
    uri: NotRequired[str]
