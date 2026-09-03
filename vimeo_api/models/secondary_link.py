from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SecondaryLink(SdkBaseModel):
    """The attributes of the secondary link."""

    label: Optional[str] = UNSET
    """The text of the secondary link."""

    link: Optional[str] = UNSET
    """The URL of the secondary link."""


class SecondaryLinkDict(TypedDict):
    label: NotRequired[str]
    link: NotRequired[str]
