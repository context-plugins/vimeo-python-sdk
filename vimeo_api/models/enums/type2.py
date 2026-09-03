from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type2(str, Enum):
    """The authenticated user's account type.

    Option descriptions:
     * ``advanced`` - The user has a Vimeo Advanced account.
     * ``basic`` - The user has a Vimeo Basic account.
     * ``business`` - The user has a Vimeo Business account.
     * ``creator`` - The user has a Vimeo Creator account.
     * ``custom`` - The user has a Vimeo Custom account.
     * ``enterprise`` - The user has a Vimeo Enterprise account.
     * ``free`` - The user has a Vimeo Free account.
     * ``live_business`` - The user has a Vimeo Business Live account.
     * ``live_premium`` - The user has a Vimeo Premium account.
     * ``live_pro`` - The user has a Vimeo Pro Live account.
     * ``ott_custom`` - The user has a Vimeo OTT Custom account.
     * ``plus`` - The user has a Vimeo Plus account.
     * ``pro`` - The user has a Vimeo Pro account.
     * ``pro_unlimited`` - The user has a Vimeo Pro Unlimited account.
     * ``producer`` - The user has a Vimeo Producer account.
     * ``production`` - The user has a Vimeo Production account.
     * ``professional`` - The user has a Vimeo Professional account.
     * ``standard`` - The user has a Vimeo Standard account.
     * ``starter`` - The user has a Vimeo Starter account.
     * ``studio`` - The user has a Vimeo Studio account."""

    ADVANCED = "advanced"
    BASIC = "basic"
    BUSINESS = "business"
    CREATOR = "creator"
    CUSTOM = "custom"
    ENTERPRISE = "enterprise"
    FREE = "free"
    LIVE_BUSINESS = "live_business"
    LIVE_PREMIUM = "live_premium"
    LIVE_PRO = "live_pro"
    OTT_CUSTOM = "ott_custom"
    PLUS = "plus"
    PRO = "pro"
    PRO_UNLIMITED = "pro_unlimited"
    PRODUCER = "producer"
    PRODUCTION = "production"
    PROFESSIONAL = "professional"
    STANDARD = "standard"
    STARTER = "starter"
    STUDIO = "studio"

    __str__ = str.__str__


Type2OrStr: TypeAlias = Annotated[Type2 | str, open_enum_validator(Type2)]
