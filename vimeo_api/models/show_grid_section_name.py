from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowGridSectionName(SdkBaseModel):
    """Information about showing the section names."""

    is_upgrade: bool
    """Whether an upgrade is required to show the section names."""

    value: bool
    """Whether to show the section names."""


class ShowGridSectionNameDict(TypedDict):
    is_upgrade: bool
    value: bool
