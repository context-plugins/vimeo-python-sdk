from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .billing import Billing, BillingDict
from .renewal import Renewal, RenewalDict
from .trial import Trial, TrialDict


class Subscription3(SdkBaseModel):
    """Information about the authenticated user's Vimeo subscription."""

    billing: Billing
    """Information about the authenticated user's subscription billing."""

    renewal: Renewal
    """Information about the authenticated user's next renewal."""

    trial: Trial
    """Information about the authenticated user's trial."""


class Subscription3Dict(TypedDict):
    billing: BillingDict
    renewal: RenewalDict
    trial: TrialDict
