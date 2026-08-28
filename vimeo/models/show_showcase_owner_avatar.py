from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowShowcaseOwnerAvatar(SdkBaseModel):
    """Information about showing the showcase owner's avatar."""

    is_upgrade: bool
    """Whether an upgrade is required to show the showcase owner's avatar."""

    value: bool
    """Whether to show the showcase owner's avatar."""


class ShowShowcaseOwnerAvatarDict(TypedDict):
    is_upgrade: bool
    value: bool
