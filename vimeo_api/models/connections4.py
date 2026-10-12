from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .albums1 import Albums1, Albums1Dict
from .ancestor_path import AncestorPath, AncestorPathDict
from .available_albums import AvailableAlbums, AvailableAlbumsDict
from .available_channels import AvailableChannels, AvailableChannelsDict
from .comments1 import Comments1, Comments1Dict
from .credits import Credits, CreditsDict
from .likes1 import Likes1, Likes1Dict
from .ondemand import Ondemand, OndemandDict
from .pictures1 import Pictures1, Pictures1Dict
from .publish_to_social import PublishToSocial, PublishToSocialDict
from .recommendations import Recommendations, RecommendationsDict
from .related import Related, RelatedDict
from .resource_creator_team_user import ResourceCreatorTeamUser, ResourceCreatorTeamUserDict
from .season import Season, SeasonDict
from .team_permissions import TeamPermissions, TeamPermissionsDict
from .texttracks import Texttracks, TexttracksDict
from .trailer import Trailer, TrailerDict
from .users_with_access import UsersWithAccess, UsersWithAccessDict
from .versions import Versions, VersionsDict


class Connections4(SdkBaseModel):
    """A list of resource URIs related to the video."""

    albums: Optional[Albums1] = UNSET
    """Information about the showcases that contain the video. This data requires a bearer token with the ``private``
    scope."""

    ancestor_path: list[AncestorPath]
    """Information about the video's ancestry, ordered from the direct parent folder to higher-level ancestors."""

    available_albums: Optional[AvailableAlbums] = UNSET
    """Information about the available showcases, or the showcases to which the video can be added. This data requires a
    bearer token with the ``private`` scope."""

    available_channels: Optional[AvailableChannels] = UNSET
    """Information about the channels to which the video can be added. This data requires a bearer token with the
    ``private`` scope."""

    comments: Comments1
    """Information about the comments on the video."""

    credits: Credits | None
    """Information about the users credited in the video."""

    likes: Likes1
    """Information about the users who have liked the video."""

    ondemand: Optional[Ondemand] = UNSET
    """Information about the video's On Demand data."""

    pictures: Pictures1
    """Information about the video's thumbnails."""

    publish_to_social: Optional[PublishToSocial] = UNSET
    """Information about the user's publish-to-social history for the video."""

    recommendations: Recommendations | None
    """Information about the recommendations for the video."""

    related: Related | None
    """Information about the video's related content."""

    resource_creator_team_user: ResourceCreatorTeamUser
    """Information about the team user who uploaded the video. This data requires a bearer token with the ``private``
    scope."""

    season: Optional[Season] = UNSET
    """Information about the video's season."""

    team_permissions: Optional[TeamPermissions] = UNSET
    """Information about the video's team permissions list. This data requires a bearer token with the ``private``
    scope."""

    texttracks: Texttracks
    """Information about the video's text tracks."""

    trailer: Optional[Trailer] = UNSET
    """Information about the video's Vimeo On Demand trailer."""

    users_with_access: Optional[UsersWithAccess] = UNSET
    """Information about the user privacy of the video, if the video privacy setting is ``users``."""

    versions: Versions
    """Information about the video's versions."""


class Connections4Dict(TypedDict):
    albums: NotRequired[Albums1Dict]
    ancestor_path: list[AncestorPathDict]
    available_albums: NotRequired[AvailableAlbumsDict]
    available_channels: NotRequired[AvailableChannelsDict]
    comments: Comments1Dict
    credits: CreditsDict | None
    likes: Likes1Dict
    ondemand: NotRequired[OndemandDict]
    pictures: Pictures1Dict
    publish_to_social: NotRequired[PublishToSocialDict]
    recommendations: RecommendationsDict | None
    related: RelatedDict | None
    resource_creator_team_user: ResourceCreatorTeamUserDict
    season: NotRequired[SeasonDict]
    team_permissions: NotRequired[TeamPermissionsDict]
    texttracks: TexttracksDict
    trailer: NotRequired[TrailerDict]
    users_with_access: NotRequired[UsersWithAccessDict]
    versions: VersionsDict
