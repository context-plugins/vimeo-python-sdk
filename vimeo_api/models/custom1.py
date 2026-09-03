from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Custom1(SdkBaseModel):
    """A collection of information relating to custom logos in the onsite player."""

    active: Optional[bool] = UNSET
    """Whether the custom logo appears in the video page player."""

    link: OptionalNullable[str] = UNSET
    """The URL that loads upon clicking the custom logo."""

    sticky: Optional[bool] = UNSET
    """Whether the custom logo appears even when the player interface is hidden."""

    url: OptionalNullable[str] = UNSET
    """The URL of the selected custom logo."""

    use_link: Optional[bool] = UNSET
    """Whether the custom logo should use the URL link."""


class Custom1Dict(TypedDict):
    active: NotRequired[bool]
    link: NotRequired[str | None]
    sticky: NotRequired[bool]
    url: NotRequired[str | None]
    use_link: NotRequired[bool]
