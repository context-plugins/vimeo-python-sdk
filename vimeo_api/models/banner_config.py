from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .show_banner import ShowBanner, ShowBannerDict
from .show_banner_description import ShowBannerDescription, ShowBannerDescriptionDict
from .show_banner_header import ShowBannerHeader, ShowBannerHeaderDict
from .show_banner_title import ShowBannerTitle, ShowBannerTitleDict
from .show_showcase_owner_avatar import ShowShowcaseOwnerAvatar, ShowShowcaseOwnerAvatarDict
from .show_start_watching_button import ShowStartWatchingButton, ShowStartWatchingButtonDict


class BannerConfig(SdkBaseModel):
    show_banner: ShowBanner
    """Information about showing the banner on the showcase page."""

    show_banner_description: ShowBannerDescription
    """Information about showing the showcase description."""

    show_banner_header: ShowBannerHeader
    """Information about showing the showcase header."""

    show_banner_title: ShowBannerTitle
    """Information about showing the showcase title."""

    show_showcase_owner_avatar: ShowShowcaseOwnerAvatar
    """Information about showing the showcase owner's avatar."""

    show_start_watching_button: ShowStartWatchingButton
    """Information about showing the button to start watching."""


class BannerConfigDict(TypedDict):
    show_banner: ShowBanner | ShowBannerDict
    show_banner_description: ShowBannerDescription | ShowBannerDescriptionDict
    show_banner_header: ShowBannerHeader | ShowBannerHeaderDict
    show_banner_title: ShowBannerTitle | ShowBannerTitleDict
    show_showcase_owner_avatar: ShowShowcaseOwnerAvatar | ShowShowcaseOwnerAvatarDict
    show_start_watching_button: ShowStartWatchingButton | ShowStartWatchingButtonDict
