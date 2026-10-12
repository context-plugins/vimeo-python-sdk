from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .currency import Currency, CurrencyDict
from .discount import Discount, DiscountDict
from .enums.tier import TierOrStr
from .id import Id, IdDict
from .metadata25 import Metadata25, Metadata25Dict
from .price import Price, PriceDict
from .price_formatted import PriceFormatted, PriceFormattedDict
from .promotion import Promotion, PromotionDict


class SubscriptionPlans(SdkBaseModel):
    currency: Currency
    """Information about the currency in which the price of the plan is expressed."""

    discount: Discount
    """Information about the plan discount."""

    id: Id
    """The SKUs of the plans."""

    metadata: Metadata25
    """The URLs and entitlements of the associated products in the store."""

    name: str
    """The name of the plan."""

    price: Price
    """Information about the prices associated with the plan."""

    price_formatted: PriceFormatted
    """The price formatted for the selected locale with the associated currency symbol."""

    promotion: Promotion
    """Information about the plan's promotion."""

    tier: TierOrStr
    """The plan type.

    Option descriptions:
     * ``advanced`` - The plan type is Vimeo Advanced.
     * ``basic`` - The plan type is Vimeo Basic.
     * ``business`` - The plan type is Vimeo Business.
     * ``core`` - The plan type is Vimeo Core.
     * ``creator`` - The plan type is Vimeo Creator.
     * ``customSelfServe`` - The plan type is Vimeo Custom.
     * ``enterprise`` - The plan type is Vimeo Enterprise.
     * ``free`` - The plan type is Vimeo Free.
     * ``livePremium`` - The plan type is Vimeo Premium.
     * ``ott`` - The plan type is Vimeo OTT.
     * ``plus`` - The plan type is Vimeo Plus.
     * ``pro`` - The plan type is Vimeo Pro.
     * ``proSolution`` - The plan type is Vimeo Pro Solution.
     * ``proUnlimited`` - The plan type is Vimeo Pro Unlimited.
     * ``production`` - The plan type is Vimeo Production.
     * ``professional`` - The plan type is Vimeo Professional.
     * ``standard`` - The plan type is Vimeo Standard.
     * ``starter`` - The plan type is Vimeo Starter.
     * ``studio`` - The plan type is Vimeo Studio.
     * ``team`` - The plan type is Vimeo Team.
     * ``teamLive`` - The plan type is Vimeo Team Live."""

    uri: str
    """The URI of the plan."""


class SubscriptionPlansDict(TypedDict):
    currency: CurrencyDict
    discount: DiscountDict
    id: IdDict
    metadata: Metadata25Dict
    name: str
    price: PriceDict
    price_formatted: PriceFormattedDict
    promotion: PromotionDict
    tier: TierOrStr
    uri: str
