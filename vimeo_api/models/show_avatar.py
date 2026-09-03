from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowAvatar(SdkBaseModel):
    """Information about showing the avatar on the showcase page."""

    is_upgrade: bool
    """Whether an upgrade is required to show the avatar on the showcase page."""

    value: bool
    """Whether to show the avatar on the showcase page."""


class ShowAvatarDict(TypedDict):
    is_upgrade: bool
    value: bool
