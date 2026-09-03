from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Embed2(SdkBaseModel):
    """Embed data for the showcase."""

    html: str | None
    """The responsive HTML code to embed the showcase's playlist on a website. This field appears only when the showcase
    has embeddable videos."""


class Embed2Dict(TypedDict):
    html: str | None
