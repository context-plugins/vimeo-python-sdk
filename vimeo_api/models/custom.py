from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Custom(SdkBaseModel):
    """A collection of information relating to custom logos in the embeddable player."""

    active: bool
    """Whether the custom logo appears in the embeddable player."""

    link: str | None
    """The URL that loads upon clicking the custom logo."""

    sticky: bool
    """Whether the custom logo appears even when the player interface is hidden."""

    url: str | None
    """The URL of the selected custom logo."""

    use_link: bool
    """Whether the custom logo should use the URL link."""


class CustomDict(TypedDict):
    active: bool
    link: str | None
    sticky: bool
    url: str | None
    use_link: bool
