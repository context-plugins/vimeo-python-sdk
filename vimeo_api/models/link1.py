from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Link1(SdkBaseModel):
    """The outro link settings. These fields appear only when **type** is ``link``."""

    name: Optional[str] = UNSET
    """The name of the outro link."""

    url: Optional[str] = UNSET
    """The URL of the outro link."""


class Link1Dict(TypedDict):
    name: NotRequired[str]
    url: NotRequired[str]
