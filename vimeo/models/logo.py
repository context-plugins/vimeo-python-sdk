from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.position1 import Position1OrStr


class Logo(SdkBaseModel):
    """Optional logo to display inline with the video title."""

    custom_logo_url: OptionalNullable[str] = UNSET
    """The canonical CDN URL of the selected custom logo, re-derived server-side from the underlying brand-kit or player
    logo."""

    enabled: Optional[bool] = UNSET
    """Whether to display the logo next to the title."""

    position: OptionalNullable[Position1OrStr] = UNSET
    """Where the logo renders relative to the title. Null until the logo is enabled."""


class LogoDict(TypedDict):
    custom_logo_url: NotRequired[str | None]
    enabled: NotRequired[bool]
    position: NotRequired[Position1OrStr | None]
