from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Button(SdkBaseModel):
    """The attributes of the button control."""

    label: Optional[str] = UNSET
    """The text of the button label."""

    link: Optional[str] = UNSET
    """The URL that loads upon clicking the button."""


class ButtonDict(TypedDict):
    label: NotRequired[str]
    link: NotRequired[str]
