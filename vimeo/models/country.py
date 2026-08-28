from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Country(SdkBaseModel):
    code: str
    """The country code in ISO-3166 format."""

    name: str
    """The name of the country."""


class CountryDict(TypedDict):
    code: str
    name: str
