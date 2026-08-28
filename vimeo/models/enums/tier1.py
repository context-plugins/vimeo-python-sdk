from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Tier1(str, Enum):
    ADVANCED = "advanced"
    BUSINESS = "business"
    FREE = "free"
    LIVE_PREMIUM = "live_premium"
    PLUS = "plus"
    PRO = "pro"
    PRO_UNLIMITED = "pro_unlimited"
    STANDARD = "standard"
    STARTER = "starter"

    __str__ = str.__str__


Tier1OrStr: TypeAlias = Annotated[Tier1 | str, open_enum_validator(Tier1)]
