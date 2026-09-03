from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Videos8(SdkBaseModel):
    """Information about the videos associated with the On Demand page."""

    extra_total: float
    """The total number of extra videos on the On Demand page."""

    main_total: float
    """The total number of main videos on the On Demand page."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of videos on this connection."""

    uri: str
    """The API URI that resolves to the connection data."""

    viewable_total: float
    """The total number of viewable videos on the On Demand page."""


class Videos8Dict(TypedDict):
    extra_total: float
    main_total: float
    options: list[str]
    total: float
    uri: str
    viewable_total: float
