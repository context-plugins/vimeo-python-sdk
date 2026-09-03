from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Disabled(SdkBaseModel):
    """Information regarding the current authenticated user's inability to access the user's profile."""

    reasons: Optional[list[str]] = UNSET
    """The reasons the current authenticated user can't access the user's profile."""


class DisabledDict(TypedDict):
    reasons: NotRequired[list[str]]
