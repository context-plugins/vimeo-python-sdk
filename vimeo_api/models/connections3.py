from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .albums import Albums, AlbumsDict
from .appearances import Appearances, AppearancesDict
from .block import Block, BlockDict
from .categories import Categories, CategoriesDict
from .channels1 import Channels1, Channels1Dict
from .connected_apps import ConnectedApps, ConnectedAppsDict
from .feed import Feed, FeedDict
from .folders_root import FoldersRoot, FoldersRootDict
from .followers import Followers, FollowersDict
from .following import Following, FollowingDict
from .groups1 import Groups1, Groups1Dict
from .import_apps import ImportApps, ImportAppsDict
from .lead_capture_form import LeadCaptureForm, LeadCaptureFormDict
from .likes import Likes, LikesDict
from .moderated_channels import ModeratedChannels, ModeratedChannelsDict
from .ms_teams_team_folder_id import MsTeamsTeamFolderId, MsTeamsTeamFolderIdDict
from .pictures import Pictures, PicturesDict
from .portfolios import Portfolios, PortfoliosDict
from .projects import Projects, ProjectsDict
from .recommended_channels import RecommendedChannels, RecommendedChannelsDict
from .recommended_users import RecommendedUsers, RecommendedUsersDict
from .shared import Shared, SharedDict
from .videos3 import Videos3, Videos3Dict
from .view_profile import ViewProfile, ViewProfileDict
from .watched_videos import WatchedVideos, WatchedVideosDict
from .watchlater import Watchlater, WatchlaterDict


class Connections3(SdkBaseModel):
    """The list of resource URIs related to the authenticated user."""

    albums: Albums
    """Information about the showcases created by the authenticated user."""

    appearances: Appearances
    """Information about the appearances of the authenticated user in other videos."""

    block: Optional[Block] = UNSET
    """Information about the users who have been blocked by the authenticated user. This data requires a bearer token
    with the ``private`` scope. This data requires a bearer token with the ``private`` scope."""

    categories: Categories
    """Information about the categories that the authenticated user is following."""

    channels: Channels1
    """Information about the channels to which the authenticated user subscribes."""

    connected_apps: Optional[ConnectedApps] = UNSET
    """Information about the authenticated user's connected apps."""

    feed: Feed
    """Information about the authenticated user's feed."""

    folders_root: FoldersRoot
    """Information about the authenticated user's root level folders and videos."""

    followers: Followers
    """Information about the authenticated user's followers."""

    following: Following
    """Information about the users who are followed by the authenticated user."""

    groups: Groups1
    """Information about the groups created by the authenticated user."""

    import_apps: Optional[ImportApps] = UNSET
    """Information about the authenticated user's auto upload apps."""

    lead_capture_form: Optional[LeadCaptureForm] = UNSET
    """Information about the authenticated user's lead capture form. This data requires a bearer token with the
    ``private`` scope."""

    likes: Likes
    """Information about the videos that the authenticated user has liked."""

    moderated_channels: ModeratedChannels
    """Information about the channels that the authenticated user moderates."""

    ms_teams_team_folder_id: OptionalNullable[MsTeamsTeamFolderId] = UNSET
    """Information about the upload folder for Microsoft Teams recordings."""

    ms_teams_tenant_token_id: OptionalNullable[str] = UNSET
    """Information about the Microsoft Teams tenant token ID."""

    pictures: Pictures
    """Information about the authenticated user's portraits."""

    portfolios: Portfolios
    """Information about the authenticated user's portfolios."""

    projects: Optional[Projects] = UNSET
    """Information about the authenticated user's projects."""

    recommended_channels: Optional[RecommendedChannels] = UNSET
    """A collection of recommended channels for the authenticated user to follow. This data requires a bearer token with
    the ``private`` scope. This data requires a bearer token with the ``private`` scope."""

    recommended_users: Optional[RecommendedUsers] = UNSET
    """A collection of recommended users for the authenticated user to follow. This data requires a bearer token with
    the ``private`` scope. This data requires a bearer token with the ``private`` scope."""

    shared: Shared
    """Information about the videos that have been shared with the authenticated user."""

    videos: Videos3
    """Information about the videos that the authenticated user has uploaded."""

    view_profile: Optional[ViewProfile] = UNSET
    """Information about the user's profile."""

    watched_videos: Optional[WatchedVideos] = UNSET
    """Information about the videos that the authenticated user has watched."""

    watchlater: Watchlater
    """Information about the videos that the authenticated user has marked to watch later."""


class Connections3Dict(TypedDict):
    albums: AlbumsDict
    appearances: AppearancesDict
    block: NotRequired[BlockDict]
    categories: CategoriesDict
    channels: Channels1Dict
    connected_apps: NotRequired[ConnectedAppsDict]
    feed: FeedDict
    folders_root: FoldersRootDict
    followers: FollowersDict
    following: FollowingDict
    groups: Groups1Dict
    import_apps: NotRequired[ImportAppsDict]
    lead_capture_form: NotRequired[LeadCaptureFormDict]
    likes: LikesDict
    moderated_channels: ModeratedChannelsDict
    ms_teams_team_folder_id: NotRequired[MsTeamsTeamFolderIdDict | None]
    ms_teams_tenant_token_id: NotRequired[str | None]
    pictures: PicturesDict
    portfolios: PortfoliosDict
    projects: NotRequired[ProjectsDict]
    recommended_channels: NotRequired[RecommendedChannelsDict]
    recommended_users: NotRequired[RecommendedUsersDict]
    shared: SharedDict
    videos: Videos3Dict
    view_profile: NotRequired[ViewProfileDict]
    watched_videos: NotRequired[WatchedVideosDict]
    watchlater: WatchlaterDict
