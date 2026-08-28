from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Recommendations(SdkBaseModel):
    """Information about the recommendations for the video."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    resource_signature: str
    """The signature for the recommendations resource."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data."""


class RecommendationsDict(TypedDict):
    options: NotRequired[list[str]]
    resource_signature: str
    uri: NotRequired[str]
