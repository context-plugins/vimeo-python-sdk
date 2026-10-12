from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .banner_config import BannerConfig, BannerConfigDict
from .layout_config import LayoutConfig, LayoutConfigDict
from .navigation_config import NavigationConfig, NavigationConfigDict
from .playback_config import PlaybackConfig, PlaybackConfigDict
from .show_account_name import ShowAccountName, ShowAccountNameDict
from .show_avatar import ShowAvatar, ShowAvatarDict
from .show_video_description import ShowVideoDescription, ShowVideoDescriptionDict
from .show_video_details import ShowVideoDetails, ShowVideoDetailsDict
from .show_video_player_cards import ShowVideoPlayerCards, ShowVideoPlayerCardsDict
from .show_video_title import ShowVideoTitle, ShowVideoTitleDict
from .text_cta_alignment import TextCtaAlignment, TextCtaAlignmentDict


class ShowcaseConfig(SdkBaseModel):
    banner: BannerConfig
    """An object containing the showcase's banner display settings."""

    layout: LayoutConfig
    """An object containing the showcase's layout display settings."""

    navigation: NavigationConfig
    """An object containing the showcase's navigation display settings."""

    playback: PlaybackConfig
    """An object containing the showcase's playback display settings."""

    show_account_name: ShowAccountName
    """Information about showing the account name on the showcase page."""

    show_avatar: ShowAvatar
    """Information about showing the avatar on the showcase page."""

    show_video_description: ShowVideoDescription
    """Information about showing the description on the showcase page."""

    show_video_details: ShowVideoDetails
    """Information about showing video details on the showcase page."""

    show_video_player_cards: ShowVideoPlayerCards
    """Information about showing video player cards on the showcase page."""

    show_video_title: ShowVideoTitle
    """Information about showing the title on the showcase page."""

    text_cta_alignment: TextCtaAlignment
    """Information about the alignment of the call-to-action text on the showcase page."""


class ShowcaseConfigDict(TypedDict):
    banner: BannerConfigDict
    layout: LayoutConfigDict
    navigation: NavigationConfigDict
    playback: PlaybackConfigDict
    show_account_name: ShowAccountNameDict
    show_avatar: ShowAvatarDict
    show_video_description: ShowVideoDescriptionDict
    show_video_details: ShowVideoDetailsDict
    show_video_player_cards: ShowVideoPlayerCardsDict
    show_video_title: ShowVideoTitleDict
    text_cta_alignment: TextCtaAlignmentDict
