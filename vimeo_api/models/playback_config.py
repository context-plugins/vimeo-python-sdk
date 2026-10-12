from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enable_ask_ai import EnableAskAi, EnableAskAiDict
from .enable_comments import EnableComments, EnableCommentsDict
from .enable_download import EnableDownload, EnableDownloadDict
from .enable_like import EnableLike, EnableLikeDict
from .enable_share import EnableShare, EnableShareDict
from .playback_grid_size import PlaybackGridSize, PlaybackGridSizeDict
from .show_playback_added_date import ShowPlaybackAddedDate, ShowPlaybackAddedDateDict
from .show_playback_grid_profile_image import ShowPlaybackGridProfileImage, ShowPlaybackGridProfileImageDict
from .show_playback_grid_profile_name import ShowPlaybackGridProfileName, ShowPlaybackGridProfileNameDict
from .show_playback_grid_video_card import ShowPlaybackGridVideoCard, ShowPlaybackGridVideoCardDict
from .show_playback_grid_video_title import ShowPlaybackGridVideoTitle, ShowPlaybackGridVideoTitleDict
from .show_playback_profile_image import ShowPlaybackProfileImage, ShowPlaybackProfileImageDict
from .show_playback_profile_name import ShowPlaybackProfileName, ShowPlaybackProfileNameDict
from .show_playback_uploaded_date import ShowPlaybackUploadedDate, ShowPlaybackUploadedDateDict
from .show_playback_video_count import ShowPlaybackVideoCount, ShowPlaybackVideoCountDict
from .show_playback_video_description import ShowPlaybackVideoDescription, ShowPlaybackVideoDescriptionDict
from .show_playback_video_title import ShowPlaybackVideoTitle, ShowPlaybackVideoTitleDict
from .show_playback_views import ShowPlaybackViews, ShowPlaybackViewsDict


class PlaybackConfig(SdkBaseModel):
    enable_ask_ai: EnableAskAi
    """Information about enabling the Ask AI functionality during playback."""

    enable_comments: EnableComments
    """Information about enabling the comments functionality during playback."""

    enable_download: EnableDownload
    """Information about enabling the download functionality during playback."""

    enable_like: EnableLike
    """Information about enabling the like functionality during playback."""

    enable_share: EnableShare
    """Information about enabling the share functionality during playback."""

    playback_grid_size: PlaybackGridSize
    """Information about the grid size configuration for playback view."""

    show_playback_added_date: ShowPlaybackAddedDate
    """Information about showing the date when the video was added during playback."""

    show_playback_grid_profile_image: ShowPlaybackGridProfileImage
    """Information about showing the profile image in grid view."""

    show_playback_grid_profile_name: ShowPlaybackGridProfileName
    """Information about showing the profile name in grid view."""

    show_playback_grid_video_card: ShowPlaybackGridVideoCard
    """Information about showing the video card in grid view."""

    show_playback_grid_video_title: ShowPlaybackGridVideoTitle
    """Information about showing the video title in grid view."""

    show_playback_profile_image: ShowPlaybackProfileImage
    """Information about showing the profile image during playback."""

    show_playback_profile_name: ShowPlaybackProfileName
    """Information about showing the profile name during playback."""

    show_playback_uploaded_date: ShowPlaybackUploadedDate
    """Information about showing the date when the video was uploaded during playback."""

    show_playback_video_count: ShowPlaybackVideoCount
    """Information about showing the video count during playback."""

    show_playback_video_description: ShowPlaybackVideoDescription
    """Information about showing the video description during playback."""

    show_playback_video_title: ShowPlaybackVideoTitle
    """Information about showing the video title during playback."""

    show_playback_views: ShowPlaybackViews
    """Information about showing the view count during playback."""


class PlaybackConfigDict(TypedDict):
    enable_ask_ai: EnableAskAiDict
    enable_comments: EnableCommentsDict
    enable_download: EnableDownloadDict
    enable_like: EnableLikeDict
    enable_share: EnableShareDict
    playback_grid_size: PlaybackGridSizeDict
    show_playback_added_date: ShowPlaybackAddedDateDict
    show_playback_grid_profile_image: ShowPlaybackGridProfileImageDict
    show_playback_grid_profile_name: ShowPlaybackGridProfileNameDict
    show_playback_grid_video_card: ShowPlaybackGridVideoCardDict
    show_playback_grid_video_title: ShowPlaybackGridVideoTitleDict
    show_playback_profile_image: ShowPlaybackProfileImageDict
    show_playback_profile_name: ShowPlaybackProfileNameDict
    show_playback_uploaded_date: ShowPlaybackUploadedDateDict
    show_playback_video_count: ShowPlaybackVideoCountDict
    show_playback_video_description: ShowPlaybackVideoDescriptionDict
    show_playback_video_title: ShowPlaybackVideoTitleDict
    show_playback_views: ShowPlaybackViewsDict
