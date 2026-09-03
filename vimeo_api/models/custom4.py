from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Custom4(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether to show the custom logo on the embed player."""

    link: Optional[str] = UNSET
    """The URL that loads when the user clicks the custom logo."""

    sticky: Optional[bool] = UNSET
    """Whether to show the custom logo persistently (``true``) or hide it with the rest of the UI (``false``)."""


class Custom4Dict(TypedDict):
    active: NotRequired[bool]
    link: NotRequired[str]
    sticky: NotRequired[bool]
