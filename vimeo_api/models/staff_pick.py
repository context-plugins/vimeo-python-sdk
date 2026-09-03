from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class StaffPick(SdkBaseModel):
    best_of_the_month: bool
    """Whether the video is a Vimeo Staff Pick Best of the Month."""

    best_of_the_year: bool
    """Whether the video is a Vimeo Staff Pick Best of the Year."""

    normal: bool
    """Whether the video is a Vimeo Staff Pick."""

    premiere: bool
    """Whether the video is a Vimeo Staff Pick Premiere."""


class StaffPickDict(TypedDict):
    best_of_the_month: bool
    best_of_the_year: bool
    normal: bool
    premiere: bool
