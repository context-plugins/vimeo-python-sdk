from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .disabled1 import Disabled1, Disabled1Dict


class Albums1(SdkBaseModel):
    """Information about the showcases that contain the video. This data requires a bearer token with the ``private``
    scope."""

    disabled: Optional[Disabled1] = UNSET
    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""

    total: Optional[float] = UNSET
    """The total number of showcases on this connection. This data requires a bearer token with the ``private``
    scope."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data. This data requires a bearer token with the ``private``
    scope."""


class Albums1Dict(TypedDict):
    disabled: NotRequired[Disabled1Dict]
    options: NotRequired[list[str]]
    total: NotRequired[float]
    uri: NotRequired[str]
