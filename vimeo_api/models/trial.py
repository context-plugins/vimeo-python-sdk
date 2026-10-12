from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status1 import Status1OrStr


class Trial(SdkBaseModel):
    """Information about the authenticated user's trial."""

    has_been_in_free_trial: bool
    """Whether the authenticated user has been in (or is currently in) a free trial. The user might not be eligible for
    a free trial even when the value of this field is ``false``."""

    is_reverse_free_trial: bool
    """Whether the user is currently in a Reverse free trial. Reverse trials are no-card trials granted before purchase
    and have no PaymentsService subscription backing them; for these users, ``subscription.renewal.renewal_date``
    carries the trial-expiry datetime instead of a next-charge datetime."""

    status: Status1OrStr | None
    """The status of the authenticated user's trial.

    Option descriptions:
     * ``free_trial`` - The user is currently in a free trial."""


class TrialDict(TypedDict):
    has_been_in_free_trial: bool
    is_reverse_free_trial: bool
    status: Status1OrStr | None
