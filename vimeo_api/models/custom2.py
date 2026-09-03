from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Custom2(SdkBaseModel):
    """A collection of information relating to custom logos in the embeddable player."""

    active: bool
    """Whether the custom logo appears in the embeddable player."""

    link: str
    """The URL that loads upon clicking the custom logo."""

    sticky: bool
    """Whether the custom logo appears even when the player interface is hidden."""

    url: str
    """The URL source of the custom player logo."""

    use_link: bool
    """Whether the custom logo should use the URL link."""


class Custom2Dict(TypedDict):
    active: bool
    link: str
    sticky: bool
    url: str
    use_link: bool
