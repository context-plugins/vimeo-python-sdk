from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowAccountName(SdkBaseModel):
    """Information about showing the account name on the showcase page."""

    is_upgrade: bool
    """Whether an upgrade is required to show the account name on the showcase page."""

    value: bool
    """Whether to show the account name on the showcase page."""


class ShowAccountNameDict(TypedDict):
    is_upgrade: bool
    value: bool
