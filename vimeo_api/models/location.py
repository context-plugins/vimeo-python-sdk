from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Location(SdkBaseModel):
    city: str | None
    """The authenticated user's city."""

    country: str | None
    """The authenticated user's country."""

    country_iso_code: str
    """The ISO code of the authenticated user's country."""

    formatted_address: str
    """The authenticated user's formatted address string."""

    latitude: float
    """The authenticated user's latitude."""

    longitude: float
    """The authenticated user's longitude."""

    neighborhood: str | None
    """The authenticated user's neighborhood."""

    state: str | None
    """The authenticated user's state."""

    state_iso_code: str | None
    """The ISO code of the authenticated user's state."""

    sub_locality: str | None
    """The authenticated user's sub-locality."""


class LocationDict(TypedDict):
    city: str | None
    country: str | None
    country_iso_code: str
    formatted_address: str
    latitude: float
    longitude: float
    neighborhood: str | None
    state: str | None
    state_iso_code: str | None
    sub_locality: str | None
