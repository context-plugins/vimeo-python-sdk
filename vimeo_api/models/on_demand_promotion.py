from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.access_type import AccessTypeOrStr
from .enums.discount_type import DiscountTypeOrStr
from .enums.product_type import ProductTypeOrStr
from .enums.stream_period import StreamPeriodOrStr
from .enums.type18 import Type18OrStr
from .metadata19 import Metadata19, Metadata19Dict


class OnDemandPromotion(SdkBaseModel):
    access_type: AccessTypeOrStr
    """The type of access that the promotion grants.

    Option descriptions:
     * ``default`` - The promotion grants discounts on existing product offerings.
     * ``vip`` - The promotion grants free access to On Demand content before it's released, or to access types that
            aren't part of the existing product offerings."""

    discount_type: DiscountTypeOrStr
    """The type of discount that the promotion provides.

    Option descriptions:
     * ``dollars`` - The promotion discounts a fixed amount from the full purchase price.
     * ``free`` - The promotion discounts the full purchase price. When **access_type** is ``vip``, **discount_type** is
            always ``free``.
     * ``percent`` - The promotion discounts a percentage of the full purchase price."""

    download: bool
    """Whether the promotion grants download access to On Demand content."""

    label: str | None
    """The prefix string for batch codes, or the null value for single codes."""

    metadata: Metadata19
    """The video's metadata."""

    percent_off: float
    """When **discount_type** is ``percent``, the percentage amount that is deducted from the product price."""

    product_type: ProductTypeOrStr
    """The type of product to which the promotion can be applied. Only the ``buy`` and ``rent`` options are available
    when **access_type** is ``vip``.

    Option descriptions:
     * ``any`` - The promotion can be applied to any product.
     * ``buy`` - The promotion can be applied to a buyable single video.
     * ``buy_episode`` - The promotion can be applied to a buyable single episode.
     * ``rent`` - The promotion can be applied to a rentable single video.
     * ``rent_episode`` - The promotion can be applied to a rentable single episode.
     * ``subscribe`` - The promotion can be applied to a subscription."""

    stream_period: StreamPeriodOrStr | None
    """The amount of time that the user has access to the On Demand content after redeeming a promotional code.

    Option descriptions:
     * ``1_week`` - Access lasts for one week.
     * ``1_year`` - Access lasts for one year.
     * ``3_month`` - Access lasts for three months.
     * ``6_month`` - Access lasts for six months.
     * ``24_hour`` - Access lasts for 24 hours.
     * ``30_days`` - Access lasts for 30 days.
     * ``48_hour`` - Access lasts for 48 hours.
     * ``72_hour`` - Access lasts for 72 hours."""

    total: float
    """When **type** is ``single``, the total number of times that the promotion can be used. When **type** is ``batch``
    or ``batch_prefix``, the total number of promo codes that have been generated."""

    type_: Type18OrStr = Field(alias="type")
    """The way in which the promotion generates promo codes.

    Option descriptions:
     * ``batch`` - The promotion provides a unique promotional code for each user.
     * ``batch_prefix`` - Like ``batch``, except that all codes have a similar prefix string. _This option is
            deprecated, yet it may still appear for some users._
     * ``single`` - The promotion provides a single promotional code for all users."""

    uri: str
    """The promotion's canonical relative URI."""


class OnDemandPromotionDict(TypedDict):
    access_type: AccessTypeOrStr
    discount_type: DiscountTypeOrStr
    download: bool
    label: str | None
    metadata: Metadata19 | Metadata19Dict
    percent_off: float
    product_type: ProductTypeOrStr
    stream_period: StreamPeriodOrStr | None
    total: float
    type_: Type18OrStr
    uri: str
