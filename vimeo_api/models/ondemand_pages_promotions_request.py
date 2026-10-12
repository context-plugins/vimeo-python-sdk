from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.access_type1 import AccessType1OrStr
from .enums.discount_type1 import DiscountType1OrStr
from .enums.product_type1 import ProductType1OrStr
from .enums.stream_period1 import StreamPeriod1OrStr
from .enums.type41 import Type41OrStr


class OndemandPagesPromotionsRequest(SdkBaseModel):
    access_type: Optional[AccessType1OrStr] = UNSET
    """The promotion access type, which is a purchase option that isn't available in the On Demand container. Use the
    **download** and **stream_period** parameters to define additional characteristics for the ``vip`` type.

    Option descriptions:
     * ``default`` - The promotion grants a discount on the existing purchase options for an On Demand container.
     * ``vip`` - The promotion grants free access to On Demand content before it's released."""

    code: Optional[str] = UNSET
    """The promotion code. This parameter is ignored when the promotion type is ``batch``."""

    discount_type: Optional[DiscountType1OrStr] = UNSET
    """The type of discount offered by the promotion code. When **access_type** is ``vip``, the value of this parameter
    must be ``free``.

    Option descriptions:
     * ``free`` - The discount reduces the price to zero.
     * ``percent`` - The discount reduces the price by the percentage defined in the **percent_off** parameter."""

    download: bool
    """Whether the promotion grants download access to On Demand content. This field is required only when the download
    access hasn't been defined in the On Demand container, or when **access_type** is ``vip`` or **product_type** is
    ``buy``."""

    end_time: Optional[str] = UNSET
    """The time at which the promotion period ends. If this parameter has no value, the promotion never expires."""

    label: Optional[str] = UNSET
    """The description of the promotion when the promotion type is ``batch``. This parameter is ignored when the
    promotion type is ``single``."""

    percent_off: Optional[float] = UNSET
    """The percentage of the discount. This parameter is applicable only when **discount_type** is ``percent``."""

    product_type: Optional[ProductType1OrStr] = UNSET
    """The type of transaction to which the promotion applies. When **access_type** is ``default``, the default value is
    ``any``. When **access_type** is ``vip``, the default value is ``rent`` and the only valid product types are ``buy``
    and ``rent``.

    Option descriptions:
     * ``any`` - The promotion applies to any transaction.
     * ``buy`` - The promotion applies only to purchased products.
     * ``buy_episode`` - The promotion applies only to purchased episodes.
     * ``rent`` - The promotion applies only to rented products.
     * ``rent_episode`` - The promotion applies only to rented episodes.
     * ``subscribe`` - The promotion applies only to subscriptions."""

    start_time: Optional[str] = UNSET
    """The time at which the promotion period starts. If this parameter has no value, the start time defaults to the
    time at which the promotion was created."""

    stream_period: StreamPeriod1OrStr
    """The amount of time for which the user can access On Demand content upon redeeming a promotion code. This
    parameter is required only when the streaming period isn't defined in the On Demand container, or when creating
    promotions where **access_type** is ``vip`` or **product_type** is ``rent``.

    Option descriptions:
     * ``1_week`` - The user can access On Demand content for a maximum of 1 week after redeeming a promotion code.
     * ``1_year`` - The user can access On Demand content for a maximum of 1 year after redeeming a promotion code.
     * ``3_month`` - The user can access On Demand content for a maximum of 3 months after redeeming a promotion code.
     * ``6_month`` - The user can access On Demand content for a maximum of 6 months after redeeming a promotion code.
     * ``24_hour`` - The user can access On Demand content for a maximum of 24 hours after redeeming a promotion code.
     * ``30_day`` - The user can access On Demand content for a maximum of 30 days after redeeming a promotion code.
     * ``48_hour`` - The user can access On Demand content for a maximum of 48 hours after redeeming a promotion code.
     * ``72_hour`` - The user can access On Demand content for a maximum of 72 hours after redeeming a promotion
            code."""

    total: float
    """When **type** is ``batch``, the total number of promotions to generate. When **type** is ``single``, the total
    number of uses of the promotion."""

    type_: Type41OrStr = Field(alias="type")
    """The type of the promotion. When **access_type** is ``vip``, the value for this parameter must be ``batch``.

    Option descriptions:
     * ``batch`` - The promotion type that generates many random codes to use one time each.
     * ``single`` - The promotion type that generates one code to use many times."""


class OndemandPagesPromotionsRequestDict(TypedDict):
    access_type: NotRequired[AccessType1OrStr]
    code: NotRequired[str]
    discount_type: NotRequired[DiscountType1OrStr]
    download: bool
    end_time: NotRequired[str]
    label: NotRequired[str]
    percent_off: NotRequired[float]
    product_type: NotRequired[ProductType1OrStr]
    start_time: NotRequired[str]
    stream_period: StreamPeriod1OrStr
    total: float
    type_: Type41OrStr
