from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class HlsDashVideoFile(SdkBaseModel):
    link: str | None
    """The direct link to the video file."""

    link_expiration_time: str
    """The time in ISO 8601 format when the link to the video file expires."""

    log: OptionalNullable[str] = UNSET
    """The URL for logging events."""


class HlsDashVideoFileDict(TypedDict):
    link: str | None
    link_expiration_time: str
    log: NotRequired[str | None]
