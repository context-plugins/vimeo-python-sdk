from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customization import Customization, CustomizationDict
from .player import Player, PlayerDict


class VideoPageSettings(SdkBaseModel):
    ask_ai: bool
    """Whether to display the button for Vimeo AI on the video page."""

    categories: bool
    """Whether to display video categories on the video page."""

    chapters: Optional[bool] = UNSET
    """Whether to display the button for chapters on the video page."""

    collections: bool
    """Whether to display collections on the video page."""

    comments: bool
    """Whether to display comments on the video page."""

    creative_commons: bool
    """Whether to display the video's Creative Commons license on the video page."""

    credits: bool
    """Whether to display credits for the video on the video page."""

    customization: Optional[Customization] = UNSET
    """The contents of the page customization group (background color, title font, and inline logo)."""

    date_added: bool
    """Whether to display the date when the video was added on the video page."""

    description: bool
    """Whether to display the video's description on the video page."""

    download: bool
    """Whether to display the button for downloads on the video page."""

    like: bool
    """Whether to display the button for likes on the video page."""

    owner: bool
    """Whether to display the video owner's user name on the video page."""

    player: Optional[Player] = UNSET
    """The contents of the player group."""

    portrait: bool
    """Whether to display the video owner's avatar on the video page."""

    share: bool
    """Whether to display the button for shares on the video page."""

    tags: bool
    """Whether to display tags for the video on the video page."""

    title: Optional[bool] = UNSET
    """Whether to display the video title on the video page."""

    transcript: Optional[bool] = UNSET
    """Whether to display the button for transcripts on the video page."""

    uploader: bool
    """Whether to display the video's uploader on the video page."""

    uri: Optional[str] = UNSET
    """The URI of the page preset."""

    views: bool
    """Whether to display the number of views that the video has received on the video page."""

    watch_later: bool
    """Whether to display the button for watching later on the video page."""


class VideoPageSettingsDict(TypedDict):
    ask_ai: bool
    categories: bool
    chapters: NotRequired[bool]
    collections: bool
    comments: bool
    creative_commons: bool
    credits: bool
    customization: NotRequired[CustomizationDict]
    date_added: bool
    description: bool
    download: bool
    like: bool
    owner: bool
    player: NotRequired[PlayerDict]
    portrait: bool
    share: bool
    tags: bool
    title: NotRequired[bool]
    transcript: NotRequired[bool]
    uploader: bool
    uri: NotRequired[str]
    views: bool
    watch_later: bool
