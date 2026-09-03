from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Buttons1(SdkBaseModel):
    embed: bool
    """Whether the preset includes settings for the embed button."""

    fullscreen: bool
    """Whether the preset includes settings for the fullscreen button."""

    hd: bool
    """Whether the preset includes settings for the HD button."""

    like: bool
    """Whether the preset includes settings for the like button."""

    reaction: OptionalNullable[bool] = UNSET
    """Whether the preset includes settings for the reaction button."""

    share: bool
    """Whether the preset includes settings for the share button."""

    vote: bool
    """Whether the preset includes settings for the vote button."""

    watchlater: bool
    """Whether the preset includes settings for the watch later button."""


class Buttons1Dict(TypedDict):
    embed: bool
    fullscreen: bool
    hd: bool
    like: bool
    reaction: NotRequired[bool | None]
    share: bool
    vote: bool
    watchlater: bool
