from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price5(SdkBaseModel):
    aud: Optional[float] = Field(default=UNSET, alias="AUD")
    """The rental price of the video in Australian dollars."""

    cad: Optional[float] = Field(default=UNSET, alias="CAD")
    """The rental price of the video in Canadian dollars."""

    chf: Optional[float] = Field(default=UNSET, alias="CHF")
    """The rental price of the video in Swiss francs."""

    dkk: Optional[float] = Field(default=UNSET, alias="DKK")
    """The rental price of the video in Danish krone."""

    eur: Optional[float] = Field(default=UNSET, alias="EUR")
    """The rental price of the video in euros."""

    gbp: Optional[float] = Field(default=UNSET, alias="GBP")
    """The rental price of the video in British pounds."""

    jpy: Optional[float] = Field(default=UNSET, alias="JPY")
    """The rental price of the video in Japanese yen."""

    krw: Optional[float] = Field(default=UNSET, alias="KRW")
    """The rental price of the video in South Korean won."""

    nok: Optional[float] = Field(default=UNSET, alias="NOK")
    """The rental price of the video in Norwegian krone."""

    pln: Optional[float] = Field(default=UNSET, alias="PLN")
    """The rental price of the video in Polish zloty."""

    sek: Optional[float] = Field(default=UNSET, alias="SEK")
    """The rental price of the video in Swedish krona."""

    usd: Optional[float] = Field(default=UNSET, alias="USD")
    """When **type** is ``film``, the rental price of the video in United States dollars. When **type** is ``series``,
    the rental price of the entire collection in United States dollars."""


class Price5Dict(TypedDict):
    aud: NotRequired[float]
    cad: NotRequired[float]
    chf: NotRequired[float]
    dkk: NotRequired[float]
    eur: NotRequired[float]
    gbp: NotRequired[float]
    jpy: NotRequired[float]
    krw: NotRequired[float]
    nok: NotRequired[float]
    pln: NotRequired[float]
    sek: NotRequired[float]
    usd: NotRequired[float]
