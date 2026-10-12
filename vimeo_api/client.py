from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.api_apps_webhooks import ApiAppsWebhooks
from .apis.api_information_essentials import ApiInformationEssentials
from .apis.authentication_extras_authenticate import AuthenticationExtrasAuthenticate
from .apis.authentication_extras_convert import AuthenticationExtrasConvert
from .apis.authentication_extras_essentials import AuthenticationExtrasEssentials
from .apis.authentication_extras_exchange import AuthenticationExtrasExchange
from .apis.categories_channels import CategoriesChannels
from .apis.categories_essentials import CategoriesEssentials
from .apis.categories_groups import CategoriesGroups
from .apis.categories_users import CategoriesUsers
from .apis.categories_videos import CategoriesVideos
from .apis.channels_categories import ChannelsCategories
from .apis.channels_essentials import ChannelsEssentials
from .apis.channels_moderators import ChannelsModerators
from .apis.channels_private_channel_members import ChannelsPrivateChannelMembers
from .apis.channels_subscriptions_and_subscribers import ChannelsSubscriptionsAndSubscribers
from .apis.channels_tags import ChannelsTags
from .apis.channels_videos import ChannelsVideos
from .apis.embed_presets_custom_logos import EmbedPresetsCustomLogos
from .apis.embed_presets_essentials import EmbedPresetsEssentials
from .apis.embed_presets_folders import EmbedPresetsFolders
from .apis.embed_presets_timeline_events import EmbedPresetsTimelineEvents
from .apis.embed_presets_videos import EmbedPresetsVideos
from .apis.folders_essentials import FoldersEssentials
from .apis.folders_items import FoldersItems
from .apis.folders_videos import FoldersVideos
from .apis.groups_essentials import GroupsEssentials
from .apis.groups_subscriptions import GroupsSubscriptions
from .apis.groups_users import GroupsUsers
from .apis.groups_videos import GroupsVideos
from .apis.likes_essentials import LikesEssentials
from .apis.live_analytics import LiveAnalytics
from .apis.live_audio_tracks import LiveAudioTracks
from .apis.live_embed_privacy import LiveEmbedPrivacy
from .apis.live_essentials import LiveEssentials
from .apis.live_event_activation import LiveEventActivation
from .apis.live_event_automated_closed_captions import LiveEventAutomatedClosedCaptions
from .apis.live_event_destinations import LiveEventDestinations
from .apis.live_event_end import LiveEventEnd
from .apis.live_event_low_latency import LiveEventLowLatency
from .apis.live_event_m3_u8_playback import LiveEventM3U8Playback
from .apis.live_event_sessions import LiveEventSessions
from .apis.live_event_thumbnails import LiveEventThumbnails
from .apis.live_event_videos import LiveEventVideos
from .apis.live_graphics import LiveGraphics
from .apis.live_scenes import LiveScenes
from .apis.on_demand_backgrounds import OnDemandBackgrounds
from .apis.on_demand_essentials import OnDemandEssentials
from .apis.on_demand_genres import OnDemandGenres
from .apis.on_demand_posters import OnDemandPosters
from .apis.on_demand_promotions import OnDemandPromotions
from .apis.on_demand_purchases_and_rentals import OnDemandPurchasesAndRentals
from .apis.on_demand_regions import OnDemandRegions
from .apis.on_demand_seasons import OnDemandSeasons
from .apis.on_demand_videos import OnDemandVideos
from .apis.payments_essentials import PaymentsEssentials
from .apis.portfolios_essentials import PortfoliosEssentials
from .apis.portfolios_videos import PortfoliosVideos
from .apis.search_federated import SearchFederated
from .apis.showcases_custom_showcase_logos import ShowcasesCustomShowcaseLogos
from .apis.showcases_custom_showcase_thumbnails import ShowcasesCustomShowcaseThumbnails
from .apis.showcases_essentials import ShowcasesEssentials
from .apis.showcases_showcase_videos import ShowcasesShowcaseVideos
from .apis.subscription_plans_essentials import SubscriptionPlansEssentials
from .apis.tags_essentials import TagsEssentials
from .apis.teams_essentials import TeamsEssentials
from .apis.teams_members import TeamsMembers
from .apis.tutorial_essentials import TutorialEssentials
from .apis.users_analytics import UsersAnalytics
from .apis.users_essentials import UsersEssentials
from .apis.users_feeds import UsersFeeds
from .apis.users_followers import UsersFollowers
from .apis.users_lms import UsersLms
from .apis.users_pictures import UsersPictures
from .apis.users_search import UsersSearch
from .apis.users_watch_history import UsersWatchHistory
from .apis.videos_ai import VideosAi
from .apis.videos_animated_thumbnails import VideosAnimatedThumbnails
from .apis.videos_chapters import VideosChapters
from .apis.videos_content_ratings import VideosContentRatings
from .apis.videos_creative_commons import VideosCreativeCommons
from .apis.videos_credits import VideosCredits
from .apis.videos_embed_privacy import VideosEmbedPrivacy
from .apis.videos_essentials import VideosEssentials
from .apis.videos_fragments import VideosFragments
from .apis.videos_languages import VideosLanguages
from .apis.videos_live_m3_u8_playback import VideosLiveM3U8Playback
from .apis.videos_moderation import VideosModeration
from .apis.videos_nondestructive_trimming import VideosNondestructiveTrimming
from .apis.videos_recommendations import VideosRecommendations
from .apis.videos_showcases import VideosShowcases
from .apis.videos_tags import VideosTags
from .apis.videos_text_tracks import VideosTextTracks
from .apis.videos_thumbnails import VideosThumbnails
from .apis.videos_transcripts import VideosTranscripts
from .apis.videos_unlisted_videos import VideosUnlistedVideos
from .apis.videos_uploads import VideosUploads
from .apis.videos_versions import VideosVersions
from .apis.videos_video_comments import VideosVideoComments
from .apis.watch_later_queue_essentials import WatchLaterQueueEssentials
from .auth import AuthSchemes, Oauth2AuthorizationCodeScope, Oauth2ClientCredentialsScope
from .base_client import DEFAULT_TIMEOUT, BaseVimeoApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AuthorizationCodeCredentials,
    AuthorizationCodeCredentialsOrDict,
    AuthorizationCodeTokenSource,
    BearerAuthScheme,
    ClientCredentials,
    ClientCredentialsOrDict,
    ClientCredentialsTokenSource,
    HttpClient,
    Httpx2Client,
    OAuth2RefreshableScheme,
    OAuth2Scheme,
    RawClient,
    RefreshableTokenSource,
    RetryOptionsOrDict,
    TokenSource,
    client_secret_basic,
    no_auth,
    param,
)


class VimeoApiClient(BaseVimeoApiClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        bearer: str | None = None,
        oauth2_authorization_code: AuthorizationCodeCredentialsOrDict[Oauth2AuthorizationCodeScope] | None = None,
        oauth2_authorization_code_token_source: (
            RefreshableTokenSource[AuthorizationCodeCredentials[Oauth2AuthorizationCodeScope]] | None
        ) = None,
        oauth2_client_credentials: ClientCredentialsOrDict[Oauth2ClientCredentialsScope] | None = None,
        oauth2_client_credentials_token_source: (
            TokenSource[ClientCredentials[Oauth2ClientCredentialsScope]] | None
        ) = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout, retry_options=retry_options)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else Httpx2Client(timeout=timeout),
            retry_options=self._retry_options,
            global_headers=[
                param[str]("User-Agent", "VimeoApiClient/3.4.9 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "3.4.9"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            bearer=BearerAuthScheme(bearer) if bearer is not None else no_auth,
            oauth2_authorization_code=(
                OAuth2RefreshableScheme(
                    credentials=AuthorizationCodeCredentials[Oauth2AuthorizationCodeScope].coerce(
                        oauth2_authorization_code
                    ),
                    source=(
                        oauth2_authorization_code_token_source
                        if oauth2_authorization_code_token_source is not None
                        else AuthorizationCodeTokenSource[Oauth2AuthorizationCodeScope](
                            client=self._raw_client,
                            authorization_url=self._server.default("/oauth/authorize"),
                            token_url=self._server.default("/oauth/access_token"),
                            refresh_url=self._server.default("/oauth/access_token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if oauth2_authorization_code is not None
                else no_auth
            ),
            oauth2_client_credentials=(
                OAuth2Scheme(
                    credentials=ClientCredentials[Oauth2ClientCredentialsScope].coerce(oauth2_client_credentials),
                    source=(
                        oauth2_client_credentials_token_source
                        if oauth2_client_credentials_token_source is not None
                        else ClientCredentialsTokenSource[Oauth2ClientCredentialsScope](
                            client=self._raw_client,
                            token_url=self._server.default("/oauth/authorize/client"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if oauth2_client_credentials is not None
                else no_auth
            ),
        )

    @cached_property
    def api_apps_webhooks(self) -> ApiAppsWebhooks:
        return ApiAppsWebhooks(self._raw_client, self._server, self._auth)

    @cached_property
    def api_information_essentials(self) -> ApiInformationEssentials:
        return ApiInformationEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def authentication_extras_authenticate(self) -> AuthenticationExtrasAuthenticate:
        return AuthenticationExtrasAuthenticate(self._raw_client, self._server, self._auth)

    @cached_property
    def authentication_extras_convert(self) -> AuthenticationExtrasConvert:
        return AuthenticationExtrasConvert(self._raw_client, self._server, self._auth)

    @cached_property
    def authentication_extras_essentials(self) -> AuthenticationExtrasEssentials:
        return AuthenticationExtrasEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def authentication_extras_exchange(self) -> AuthenticationExtrasExchange:
        return AuthenticationExtrasExchange(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_channels(self) -> CategoriesChannels:
        return CategoriesChannels(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_essentials(self) -> CategoriesEssentials:
        return CategoriesEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_groups(self) -> CategoriesGroups:
        return CategoriesGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_users(self) -> CategoriesUsers:
        return CategoriesUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_videos(self) -> CategoriesVideos:
        return CategoriesVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_categories(self) -> ChannelsCategories:
        return ChannelsCategories(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_essentials(self) -> ChannelsEssentials:
        return ChannelsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_moderators(self) -> ChannelsModerators:
        return ChannelsModerators(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_private_channel_members(self) -> ChannelsPrivateChannelMembers:
        return ChannelsPrivateChannelMembers(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_subscriptions_and_subscribers(self) -> ChannelsSubscriptionsAndSubscribers:
        return ChannelsSubscriptionsAndSubscribers(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_tags(self) -> ChannelsTags:
        return ChannelsTags(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_videos(self) -> ChannelsVideos:
        return ChannelsVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def embed_presets_custom_logos(self) -> EmbedPresetsCustomLogos:
        return EmbedPresetsCustomLogos(self._raw_client, self._server, self._auth)

    @cached_property
    def embed_presets_essentials(self) -> EmbedPresetsEssentials:
        return EmbedPresetsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def embed_presets_folders(self) -> EmbedPresetsFolders:
        return EmbedPresetsFolders(self._raw_client, self._server, self._auth)

    @cached_property
    def embed_presets_timeline_events(self) -> EmbedPresetsTimelineEvents:
        return EmbedPresetsTimelineEvents(self._raw_client, self._server, self._auth)

    @cached_property
    def embed_presets_videos(self) -> EmbedPresetsVideos:
        return EmbedPresetsVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def folders_essentials(self) -> FoldersEssentials:
        return FoldersEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def folders_items(self) -> FoldersItems:
        return FoldersItems(self._raw_client, self._server, self._auth)

    @cached_property
    def folders_videos(self) -> FoldersVideos:
        return FoldersVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def groups_essentials(self) -> GroupsEssentials:
        return GroupsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def groups_subscriptions(self) -> GroupsSubscriptions:
        return GroupsSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def groups_users(self) -> GroupsUsers:
        return GroupsUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def groups_videos(self) -> GroupsVideos:
        return GroupsVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def likes_essentials(self) -> LikesEssentials:
        return LikesEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def live_analytics(self) -> LiveAnalytics:
        return LiveAnalytics(self._raw_client, self._server, self._auth)

    @cached_property
    def live_audio_tracks(self) -> LiveAudioTracks:
        return LiveAudioTracks(self._raw_client, self._server, self._auth)

    @cached_property
    def live_embed_privacy(self) -> LiveEmbedPrivacy:
        return LiveEmbedPrivacy(self._raw_client, self._server, self._auth)

    @cached_property
    def live_essentials(self) -> LiveEssentials:
        return LiveEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_m3_u8_playback(self) -> LiveEventM3U8Playback:
        return LiveEventM3U8Playback(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_activation(self) -> LiveEventActivation:
        return LiveEventActivation(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_automated_closed_captions(self) -> LiveEventAutomatedClosedCaptions:
        return LiveEventAutomatedClosedCaptions(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_destinations(self) -> LiveEventDestinations:
        return LiveEventDestinations(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_end(self) -> LiveEventEnd:
        return LiveEventEnd(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_low_latency(self) -> LiveEventLowLatency:
        return LiveEventLowLatency(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_sessions(self) -> LiveEventSessions:
        return LiveEventSessions(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_thumbnails(self) -> LiveEventThumbnails:
        return LiveEventThumbnails(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_videos(self) -> LiveEventVideos:
        return LiveEventVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def live_graphics(self) -> LiveGraphics:
        return LiveGraphics(self._raw_client, self._server, self._auth)

    @cached_property
    def live_scenes(self) -> LiveScenes:
        return LiveScenes(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_backgrounds(self) -> OnDemandBackgrounds:
        return OnDemandBackgrounds(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_essentials(self) -> OnDemandEssentials:
        return OnDemandEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_genres(self) -> OnDemandGenres:
        return OnDemandGenres(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_posters(self) -> OnDemandPosters:
        return OnDemandPosters(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_promotions(self) -> OnDemandPromotions:
        return OnDemandPromotions(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_purchases_and_rentals(self) -> OnDemandPurchasesAndRentals:
        return OnDemandPurchasesAndRentals(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_regions(self) -> OnDemandRegions:
        return OnDemandRegions(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_seasons(self) -> OnDemandSeasons:
        return OnDemandSeasons(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_videos(self) -> OnDemandVideos:
        return OnDemandVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def payments_essentials(self) -> PaymentsEssentials:
        return PaymentsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def portfolios_essentials(self) -> PortfoliosEssentials:
        return PortfoliosEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def portfolios_videos(self) -> PortfoliosVideos:
        return PortfoliosVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def search_federated(self) -> SearchFederated:
        return SearchFederated(self._raw_client, self._server, self._auth)

    @cached_property
    def showcases_custom_showcase_logos(self) -> ShowcasesCustomShowcaseLogos:
        return ShowcasesCustomShowcaseLogos(self._raw_client, self._server, self._auth)

    @cached_property
    def showcases_custom_showcase_thumbnails(self) -> ShowcasesCustomShowcaseThumbnails:
        return ShowcasesCustomShowcaseThumbnails(self._raw_client, self._server, self._auth)

    @cached_property
    def showcases_essentials(self) -> ShowcasesEssentials:
        return ShowcasesEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def showcases_showcase_videos(self) -> ShowcasesShowcaseVideos:
        return ShowcasesShowcaseVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_plans_essentials(self) -> SubscriptionPlansEssentials:
        return SubscriptionPlansEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def tags_essentials(self) -> TagsEssentials:
        return TagsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def teams_essentials(self) -> TeamsEssentials:
        return TeamsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def teams_members(self) -> TeamsMembers:
        return TeamsMembers(self._raw_client, self._server, self._auth)

    @cached_property
    def tutorial_essentials(self) -> TutorialEssentials:
        return TutorialEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def users_analytics(self) -> UsersAnalytics:
        return UsersAnalytics(self._raw_client, self._server, self._auth)

    @cached_property
    def users_essentials(self) -> UsersEssentials:
        return UsersEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def users_feeds(self) -> UsersFeeds:
        return UsersFeeds(self._raw_client, self._server, self._auth)

    @cached_property
    def users_followers(self) -> UsersFollowers:
        return UsersFollowers(self._raw_client, self._server, self._auth)

    @cached_property
    def users_lms(self) -> UsersLms:
        return UsersLms(self._raw_client, self._server, self._auth)

    @cached_property
    def users_pictures(self) -> UsersPictures:
        return UsersPictures(self._raw_client, self._server, self._auth)

    @cached_property
    def users_search(self) -> UsersSearch:
        return UsersSearch(self._raw_client, self._server, self._auth)

    @cached_property
    def users_watch_history(self) -> UsersWatchHistory:
        return UsersWatchHistory(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_ai(self) -> VideosAi:
        return VideosAi(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_animated_thumbnails(self) -> VideosAnimatedThumbnails:
        return VideosAnimatedThumbnails(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_chapters(self) -> VideosChapters:
        return VideosChapters(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_content_ratings(self) -> VideosContentRatings:
        return VideosContentRatings(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_creative_commons(self) -> VideosCreativeCommons:
        return VideosCreativeCommons(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_credits(self) -> VideosCredits:
        return VideosCredits(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_embed_privacy(self) -> VideosEmbedPrivacy:
        return VideosEmbedPrivacy(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_essentials(self) -> VideosEssentials:
        return VideosEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_fragments(self) -> VideosFragments:
        return VideosFragments(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_languages(self) -> VideosLanguages:
        return VideosLanguages(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_live_m3_u8_playback(self) -> VideosLiveM3U8Playback:
        return VideosLiveM3U8Playback(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_moderation(self) -> VideosModeration:
        return VideosModeration(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_nondestructive_trimming(self) -> VideosNondestructiveTrimming:
        return VideosNondestructiveTrimming(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_recommendations(self) -> VideosRecommendations:
        return VideosRecommendations(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_showcases(self) -> VideosShowcases:
        return VideosShowcases(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_tags(self) -> VideosTags:
        return VideosTags(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_text_tracks(self) -> VideosTextTracks:
        return VideosTextTracks(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_thumbnails(self) -> VideosThumbnails:
        return VideosThumbnails(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_transcripts(self) -> VideosTranscripts:
        return VideosTranscripts(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_unlisted_videos(self) -> VideosUnlistedVideos:
        return VideosUnlistedVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_uploads(self) -> VideosUploads:
        return VideosUploads(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_versions(self) -> VideosVersions:
        return VideosVersions(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_video_comments(self) -> VideosVideoComments:
        return VideosVideoComments(self._raw_client, self._server, self._auth)

    @cached_property
    def watch_later_queue_essentials(self) -> WatchLaterQueueEssentials:
        return WatchLaterQueueEssentials(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = VimeoApiClient
