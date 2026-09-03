from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Custom10(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether to show the active custom logo on the embeddable player."""

    link: Optional[str] = UNSET
    """The URL that loads when the user clicks the custom logo."""

    sticky: Optional[bool] = UNSET
    """Whether the custom logo is always visible on the embeddable player (``true``) or whether the logo appears and
    disappears with the rest of the UI (``false``)."""


class Custom10Dict(TypedDict):
    active: NotRequired[bool]
    link: NotRequired[str]
    sticky: NotRequired[bool]
