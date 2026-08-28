from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Display(str, Enum):
    """The authenticated user's membership level.

    Option descriptions:
     * ``Advanced`` - The user has an Advanced subscription.
     * ``Basic`` - The user has a Vimeo Basic subscription.
     * ``Business`` - The user has a Vimeo Business subscription.
     * ``Business Live`` - The user has a Vimeo Business Live subscription.
     * ``Creator`` - The user has a Vimeo Creator subscription.
     * ``Custom`` - The user has a Vimeo Custom subscription.
     * ``Free`` - The user has a Free subscription.
     * ``Ott Custom`` - The user has a Vimeo OTT Custom subscription.
     * ``Plus`` - The user has a Vimeo Plus subscription.
     * ``Premium`` - The user has a Vimeo Premium subscription.
     * ``Pro`` - The user has a Vimeo Pro subscription.
     * ``Pro Live`` - The user has a Vimeo Pro Live subscription.
     * ``Pro Unlimited`` - The user has a Vimeo Pro Unlimited subscription.
     * ``Producer`` - The user has a Vimeo Producer subscription.
     * ``Production`` - The user has a Vimeo Production subscription.
     * ``Professional`` - The user has a Vimeo Professional subscription.
     * ``Standard`` - The user has a Vimeo Standard subscription.
     * ``Starter`` - The user has a Vimeo Starter subscription.
     * ``Studio`` - The user has a Vimeo Studio subscription."""

    ADVANCED = "Advanced"
    BASIC = "Basic"
    BUSINESS = "Business"
    BUSINESS_LIVE = "Business Live"
    CREATOR = "Creator"
    CUSTOM = "Custom"
    FREE = "Free"
    OTT_CUSTOM = "Ott Custom"
    PLUS = "Plus"
    PREMIUM = "Premium"
    PRO = "Pro"
    PRO_LIVE = "Pro Live"
    PRO_UNLIMITED = "Pro Unlimited"
    PRODUCER = "Producer"
    PRODUCTION = "Production"
    PROFESSIONAL = "Professional"
    STANDARD = "Standard"
    STARTER = "Starter"
    STUDIO = "Studio"

    __str__ = str.__str__


DisplayOrStr: TypeAlias = Annotated[Display | str, open_enum_validator(Display)]
