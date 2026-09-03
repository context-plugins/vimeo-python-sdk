from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProductType(str, Enum):
    """The type of product to which the promotion can be applied. Only the ``buy`` and ``rent`` options are available
    when **access_type** is ``vip``.

    Option descriptions:
     * ``any`` - The promotion can be applied to any product.
     * ``buy`` - The promotion can be applied to a buyable single video.
     * ``buy_episode`` - The promotion can be applied to a buyable single episode.
     * ``rent`` - The promotion can be applied to a rentable single video.
     * ``rent_episode`` - The promotion can be applied to a rentable single episode.
     * ``subscribe`` - The promotion can be applied to a subscription."""

    ANY = "any"
    BUY = "buy"
    BUY_EPISODE = "buy_episode"
    RENT = "rent"
    RENT_EPISODE = "rent_episode"
    SUBSCRIBE = "subscribe"

    __str__ = str.__str__


ProductTypeOrStr: TypeAlias = Annotated[ProductType | str, open_enum_validator(ProductType)]
