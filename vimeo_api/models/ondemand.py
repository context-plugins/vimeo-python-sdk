from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Ondemand(SdkBaseModel):
    """Information about the video's On Demand data."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    resource_key: Optional[str] = UNSET
    """The On Demand connection resource key."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data."""


class OndemandDict(TypedDict):
    options: NotRequired[list[str]]
    resource_key: NotRequired[str]
    uri: NotRequired[str]
