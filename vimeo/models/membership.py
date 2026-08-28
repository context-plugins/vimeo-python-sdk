from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.display import DisplayOrStr
from .enums.type2 import Type2OrStr
from .subscription3 import Subscription3, Subscription3Dict


class Membership(SdkBaseModel):
    display: DisplayOrStr
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

    subscription: Subscription3
    """Information about the authenticated user's Vimeo subscription."""

    type_: Type2OrStr = Field(alias="type")
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


class MembershipDict(TypedDict):
    display: DisplayOrStr
    subscription: Subscription3 | Subscription3Dict
    type_: Type2OrStr
