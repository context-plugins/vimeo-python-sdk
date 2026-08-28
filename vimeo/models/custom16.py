from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Custom16(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether to show the active custom logo on the embeddable player."""

    id: OptionalNullable[float] = UNSET
    """The ID of the custom logo that will show on the emeddable player."""

    link: OptionalNullable[str] = UNSET
    """The URL that loads when the user clicks the custom logo."""

    sticky: Optional[bool] = UNSET
    """Whether the custom logo is always visible on the embeddable player (``true``) or whether the logo appears and
    disappears with the rest of the UI (``false``)."""


class Custom16Dict(TypedDict):
    active: NotRequired[bool]
    id: NotRequired[float | None]
    link: NotRequired[str | None]
    sticky: NotRequired[bool]
