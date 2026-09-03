from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AcceptedCurrencies(str, Enum):
    """An array of accepted currencies.

    Option descriptions:
     * ``AUD`` - The currency is in Australian dollars.
     * ``CAD`` - The currency is in Canadian dollars.
     * ``CHF`` - The currency is in Swiss francs.
     * ``DKK`` - The currency is in Danish krone.
     * ``EUR`` - The currency is in euros.
     * ``GBP`` - The currency is in British pounds.
     * ``JPY`` - The currency is in Japanese yen.
     * ``KRW`` - The currency is in South Korean won.
     * ``NOK`` - The currency is in Norwegian krone.
     * ``PLN`` - The currency is in Polish zloty.
     * ``SEK`` - The currency is in Swedish krona.
     * ``USD`` - The currency is in United States dollars."""

    AUD = "AUD"
    CAD = "CAD"
    CHF = "CHF"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    KRW = "KRW"
    NOK = "NOK"
    PLN = "PLN"
    SEK = "SEK"
    USD = "USD"

    __str__ = str.__str__


AcceptedCurrenciesOrStr: TypeAlias = Annotated[AcceptedCurrencies | str, open_enum_validator(AcceptedCurrencies)]
