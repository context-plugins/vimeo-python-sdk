from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Tier(str, Enum):
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

    ADVANCED = "advanced"
    BASIC = "basic"
    BUSINESS = "business"
    CORE = "core"
    CREATOR = "creator"
    CUSTOM_SELF_SERVE = "customSelfServe"
    ENTERPRISE = "enterprise"
    FREE = "free"
    LIVE_PREMIUM = "livePremium"
    OTT = "ott"
    PLUS = "plus"
    PRO = "pro"
    PRO_SOLUTION = "proSolution"
    PRO_UNLIMITED = "proUnlimited"
    PRODUCTION = "production"
    PROFESSIONAL = "professional"
    STANDARD = "standard"
    STARTER = "starter"
    STUDIO = "studio"
    TEAM = "team"
    TEAM_LIVE = "teamLive"

    __str__ = str.__str__


TierOrStr: TypeAlias = Annotated[Tier | str, open_enum_validator(Tier)]
