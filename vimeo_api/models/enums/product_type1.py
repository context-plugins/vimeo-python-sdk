from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProductType1(str, Enum):
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

    ANY = "any"
    BUY = "buy"
    BUY_EPISODE = "buy_episode"
    RENT = "rent"
    RENT_EPISODE = "rent_episode"
    SUBSCRIBE = "subscribe"

    __str__ = str.__str__


ProductType1OrStr: TypeAlias = Annotated[ProductType1 | str, open_enum_validator(ProductType1)]
