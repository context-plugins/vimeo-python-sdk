from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.api_apps_webhooks import AsyncApiAppsWebhooks
from .apis.api_information_essentials import AsyncApiInformationEssentials
from .apis.authentication_extras_authenticate import AsyncAuthenticationExtrasAuthenticate
from .apis.authentication_extras_convert import AsyncAuthenticationExtrasConvert
from .apis.authentication_extras_essentials import AsyncAuthenticationExtrasEssentials
from .apis.authentication_extras_exchange import AsyncAuthenticationExtrasExchange
from .apis.categories_channels import AsyncCategoriesChannels
from .apis.categories_essentials import AsyncCategoriesEssentials
from .apis.categories_groups import AsyncCategoriesGroups
from .apis.categories_users import AsyncCategoriesUsers
from .apis.categories_videos import AsyncCategoriesVideos
from .apis.channels_categories import AsyncChannelsCategories
from .apis.channels_essentials import AsyncChannelsEssentials
from .apis.channels_moderators import AsyncChannelsModerators
from .apis.channels_private_channel_members import AsyncChannelsPrivateChannelMembers
from .apis.channels_subscriptions_and_subscribers import AsyncChannelsSubscriptionsAndSubscribers
from .apis.channels_tags import AsyncChannelsTags
from .apis.channels_videos import AsyncChannelsVideos
from .apis.embed_presets_custom_logos import AsyncEmbedPresetsCustomLogos
from .apis.embed_presets_essentials import AsyncEmbedPresetsEssentials
from .apis.embed_presets_folders import AsyncEmbedPresetsFolders
from .apis.embed_presets_timeline_events import AsyncEmbedPresetsTimelineEvents
from .apis.embed_presets_videos import AsyncEmbedPresetsVideos
from .apis.folders_essentials import AsyncFoldersEssentials
from .apis.folders_items import AsyncFoldersItems
from .apis.folders_videos import AsyncFoldersVideos
from .apis.groups_essentials import AsyncGroupsEssentials
from .apis.groups_subscriptions import AsyncGroupsSubscriptions
from .apis.groups_users import AsyncGroupsUsers
from .apis.groups_videos import AsyncGroupsVideos
from .apis.likes_essentials import AsyncLikesEssentials
from .apis.live_analytics import AsyncLiveAnalytics
from .apis.live_audio_tracks import AsyncLiveAudioTracks
from .apis.live_embed_privacy import AsyncLiveEmbedPrivacy
from .apis.live_essentials import AsyncLiveEssentials
from .apis.live_event_activation import AsyncLiveEventActivation
from .apis.live_event_automated_closed_captions import AsyncLiveEventAutomatedClosedCaptions
from .apis.live_event_destinations import AsyncLiveEventDestinations
from .apis.live_event_end import AsyncLiveEventEnd
from .apis.live_event_low_latency import AsyncLiveEventLowLatency
from .apis.live_event_m3_u8_playback import AsyncLiveEventM3U8Playback
from .apis.live_event_sessions import AsyncLiveEventSessions
from .apis.live_event_thumbnails import AsyncLiveEventThumbnails
from .apis.live_event_videos import AsyncLiveEventVideos
from .apis.live_graphics import AsyncLiveGraphics
from .apis.live_scenes import AsyncLiveScenes
from .apis.on_demand_backgrounds import AsyncOnDemandBackgrounds
from .apis.on_demand_essentials import AsyncOnDemandEssentials
from .apis.on_demand_genres import AsyncOnDemandGenres
from .apis.on_demand_posters import AsyncOnDemandPosters
from .apis.on_demand_promotions import AsyncOnDemandPromotions
from .apis.on_demand_purchases_and_rentals import AsyncOnDemandPurchasesAndRentals
from .apis.on_demand_regions import AsyncOnDemandRegions
from .apis.on_demand_seasons import AsyncOnDemandSeasons
from .apis.on_demand_videos import AsyncOnDemandVideos
from .apis.payments_essentials import AsyncPaymentsEssentials
from .apis.portfolios_essentials import AsyncPortfoliosEssentials
from .apis.portfolios_videos import AsyncPortfoliosVideos
from .apis.search_federated import AsyncSearchFederated
from .apis.showcases_custom_showcase_logos import AsyncShowcasesCustomShowcaseLogos
from .apis.showcases_custom_showcase_thumbnails import AsyncShowcasesCustomShowcaseThumbnails
from .apis.showcases_essentials import AsyncShowcasesEssentials
from .apis.showcases_showcase_videos import AsyncShowcasesShowcaseVideos
from .apis.subscription_plans_essentials import AsyncSubscriptionPlansEssentials
from .apis.tags_essentials import AsyncTagsEssentials
from .apis.teams_essentials import AsyncTeamsEssentials
from .apis.teams_members import AsyncTeamsMembers
from .apis.tutorial_essentials import AsyncTutorialEssentials
from .apis.users_analytics import AsyncUsersAnalytics
from .apis.users_essentials import AsyncUsersEssentials
from .apis.users_feeds import AsyncUsersFeeds
from .apis.users_followers import AsyncUsersFollowers
from .apis.users_lms import AsyncUsersLms
from .apis.users_pictures import AsyncUsersPictures
from .apis.users_search import AsyncUsersSearch
from .apis.users_watch_history import AsyncUsersWatchHistory
from .apis.videos_ai import AsyncVideosAi
from .apis.videos_animated_thumbnails import AsyncVideosAnimatedThumbnails
from .apis.videos_chapters import AsyncVideosChapters
from .apis.videos_content_ratings import AsyncVideosContentRatings
from .apis.videos_creative_commons import AsyncVideosCreativeCommons
from .apis.videos_credits import AsyncVideosCredits
from .apis.videos_embed_privacy import AsyncVideosEmbedPrivacy
from .apis.videos_essentials import AsyncVideosEssentials
from .apis.videos_fragments import AsyncVideosFragments
from .apis.videos_languages import AsyncVideosLanguages
from .apis.videos_live_m3_u8_playback import AsyncVideosLiveM3U8Playback
from .apis.videos_moderation import AsyncVideosModeration
from .apis.videos_nondestructive_trimming import AsyncVideosNondestructiveTrimming
from .apis.videos_recommendations import AsyncVideosRecommendations
from .apis.videos_showcases import AsyncVideosShowcases
from .apis.videos_tags import AsyncVideosTags
from .apis.videos_text_tracks import AsyncVideosTextTracks
from .apis.videos_thumbnails import AsyncVideosThumbnails
from .apis.videos_transcripts import AsyncVideosTranscripts
from .apis.videos_unlisted_videos import AsyncVideosUnlistedVideos
from .apis.videos_uploads import AsyncVideosUploads
from .apis.videos_versions import AsyncVideosVersions
from .apis.videos_video_comments import AsyncVideosVideoComments
from .apis.watch_later_queue_essentials import AsyncWatchLaterQueueEssentials
from .auth import AsyncAuthSchemes, Oauth2AuthorizationCodeScope, Oauth2ClientCredentialsScope
from .base_client import DEFAULT_TIMEOUT, BaseVimeoClient
from .core import (
    AsyncAuthorizationCodeCredentials,
    AsyncAuthorizationCodeCredentialsOrDict,
    AsyncAuthorizationCodeTokenSource,
    AsyncClientCredentialsTokenSource,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncOAuth2RefreshableScheme,
    AsyncOAuth2Scheme,
    AsyncRawClient,
    AsyncRefreshableTokenSource,
    AsyncTokenSource,
    BearerAuthScheme,
    ClientCredentials,
    ClientCredentialsOrDict,
    client_secret_basic,
    no_auth,
)


class AsyncVimeoClient(BaseVimeoClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        bearer: str | None = None,
        oauth2_authorization_code: AsyncAuthorizationCodeCredentialsOrDict[Oauth2AuthorizationCodeScope] | None = None,
        oauth2_authorization_code_token_source: (
            AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[Oauth2AuthorizationCodeScope]] | None
        ) = None,
        oauth2_client_credentials: ClientCredentialsOrDict[Oauth2ClientCredentialsScope] | None = None,
        oauth2_client_credentials_token_source: (
            AsyncTokenSource[ClientCredentials[Oauth2ClientCredentialsScope]] | None
        ) = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
        )
        self._auth = AsyncAuthSchemes(
            bearer=BearerAuthScheme(bearer) if bearer is not None else no_auth,
            oauth2_authorization_code=(
                AsyncOAuth2RefreshableScheme(
                    credentials=AsyncAuthorizationCodeCredentials[Oauth2AuthorizationCodeScope].coerce(
                        oauth2_authorization_code
                    ),
                    source=(
                        oauth2_authorization_code_token_source
                        if oauth2_authorization_code_token_source is not None
                        else AsyncAuthorizationCodeTokenSource[Oauth2AuthorizationCodeScope](
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
                AsyncOAuth2Scheme(
                    credentials=ClientCredentials[Oauth2ClientCredentialsScope].coerce(oauth2_client_credentials),
                    source=(
                        oauth2_client_credentials_token_source
                        if oauth2_client_credentials_token_source is not None
                        else AsyncClientCredentialsTokenSource[Oauth2ClientCredentialsScope](
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
    def api_apps_webhooks(self) -> AsyncApiAppsWebhooks:
        return AsyncApiAppsWebhooks(self._raw_client, self._server, self._auth)

    @cached_property
    def api_information_essentials(self) -> AsyncApiInformationEssentials:
        return AsyncApiInformationEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def authentication_extras_authenticate(self) -> AsyncAuthenticationExtrasAuthenticate:
        return AsyncAuthenticationExtrasAuthenticate(self._raw_client, self._server, self._auth)

    @cached_property
    def authentication_extras_convert(self) -> AsyncAuthenticationExtrasConvert:
        return AsyncAuthenticationExtrasConvert(self._raw_client, self._server, self._auth)

    @cached_property
    def authentication_extras_essentials(self) -> AsyncAuthenticationExtrasEssentials:
        return AsyncAuthenticationExtrasEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def authentication_extras_exchange(self) -> AsyncAuthenticationExtrasExchange:
        return AsyncAuthenticationExtrasExchange(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_channels(self) -> AsyncCategoriesChannels:
        return AsyncCategoriesChannels(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_essentials(self) -> AsyncCategoriesEssentials:
        return AsyncCategoriesEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_groups(self) -> AsyncCategoriesGroups:
        return AsyncCategoriesGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_users(self) -> AsyncCategoriesUsers:
        return AsyncCategoriesUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def categories_videos(self) -> AsyncCategoriesVideos:
        return AsyncCategoriesVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_categories(self) -> AsyncChannelsCategories:
        return AsyncChannelsCategories(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_essentials(self) -> AsyncChannelsEssentials:
        return AsyncChannelsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_moderators(self) -> AsyncChannelsModerators:
        return AsyncChannelsModerators(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_private_channel_members(self) -> AsyncChannelsPrivateChannelMembers:
        return AsyncChannelsPrivateChannelMembers(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_subscriptions_and_subscribers(self) -> AsyncChannelsSubscriptionsAndSubscribers:
        return AsyncChannelsSubscriptionsAndSubscribers(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_tags(self) -> AsyncChannelsTags:
        return AsyncChannelsTags(self._raw_client, self._server, self._auth)

    @cached_property
    def channels_videos(self) -> AsyncChannelsVideos:
        return AsyncChannelsVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def embed_presets_custom_logos(self) -> AsyncEmbedPresetsCustomLogos:
        return AsyncEmbedPresetsCustomLogos(self._raw_client, self._server, self._auth)

    @cached_property
    def embed_presets_essentials(self) -> AsyncEmbedPresetsEssentials:
        return AsyncEmbedPresetsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def embed_presets_folders(self) -> AsyncEmbedPresetsFolders:
        return AsyncEmbedPresetsFolders(self._raw_client, self._server, self._auth)

    @cached_property
    def embed_presets_timeline_events(self) -> AsyncEmbedPresetsTimelineEvents:
        return AsyncEmbedPresetsTimelineEvents(self._raw_client, self._server, self._auth)

    @cached_property
    def embed_presets_videos(self) -> AsyncEmbedPresetsVideos:
        return AsyncEmbedPresetsVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def folders_essentials(self) -> AsyncFoldersEssentials:
        return AsyncFoldersEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def folders_items(self) -> AsyncFoldersItems:
        return AsyncFoldersItems(self._raw_client, self._server, self._auth)

    @cached_property
    def folders_videos(self) -> AsyncFoldersVideos:
        return AsyncFoldersVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def groups_essentials(self) -> AsyncGroupsEssentials:
        return AsyncGroupsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def groups_subscriptions(self) -> AsyncGroupsSubscriptions:
        return AsyncGroupsSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def groups_users(self) -> AsyncGroupsUsers:
        return AsyncGroupsUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def groups_videos(self) -> AsyncGroupsVideos:
        return AsyncGroupsVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def likes_essentials(self) -> AsyncLikesEssentials:
        return AsyncLikesEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def live_analytics(self) -> AsyncLiveAnalytics:
        return AsyncLiveAnalytics(self._raw_client, self._server, self._auth)

    @cached_property
    def live_audio_tracks(self) -> AsyncLiveAudioTracks:
        return AsyncLiveAudioTracks(self._raw_client, self._server, self._auth)

    @cached_property
    def live_embed_privacy(self) -> AsyncLiveEmbedPrivacy:
        return AsyncLiveEmbedPrivacy(self._raw_client, self._server, self._auth)

    @cached_property
    def live_essentials(self) -> AsyncLiveEssentials:
        return AsyncLiveEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_m3_u8_playback(self) -> AsyncLiveEventM3U8Playback:
        return AsyncLiveEventM3U8Playback(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_activation(self) -> AsyncLiveEventActivation:
        return AsyncLiveEventActivation(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_automated_closed_captions(self) -> AsyncLiveEventAutomatedClosedCaptions:
        return AsyncLiveEventAutomatedClosedCaptions(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_destinations(self) -> AsyncLiveEventDestinations:
        return AsyncLiveEventDestinations(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_end(self) -> AsyncLiveEventEnd:
        return AsyncLiveEventEnd(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_low_latency(self) -> AsyncLiveEventLowLatency:
        return AsyncLiveEventLowLatency(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_sessions(self) -> AsyncLiveEventSessions:
        return AsyncLiveEventSessions(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_thumbnails(self) -> AsyncLiveEventThumbnails:
        return AsyncLiveEventThumbnails(self._raw_client, self._server, self._auth)

    @cached_property
    def live_event_videos(self) -> AsyncLiveEventVideos:
        return AsyncLiveEventVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def live_graphics(self) -> AsyncLiveGraphics:
        return AsyncLiveGraphics(self._raw_client, self._server, self._auth)

    @cached_property
    def live_scenes(self) -> AsyncLiveScenes:
        return AsyncLiveScenes(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_backgrounds(self) -> AsyncOnDemandBackgrounds:
        return AsyncOnDemandBackgrounds(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_essentials(self) -> AsyncOnDemandEssentials:
        return AsyncOnDemandEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_genres(self) -> AsyncOnDemandGenres:
        return AsyncOnDemandGenres(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_posters(self) -> AsyncOnDemandPosters:
        return AsyncOnDemandPosters(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_promotions(self) -> AsyncOnDemandPromotions:
        return AsyncOnDemandPromotions(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_purchases_and_rentals(self) -> AsyncOnDemandPurchasesAndRentals:
        return AsyncOnDemandPurchasesAndRentals(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_regions(self) -> AsyncOnDemandRegions:
        return AsyncOnDemandRegions(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_seasons(self) -> AsyncOnDemandSeasons:
        return AsyncOnDemandSeasons(self._raw_client, self._server, self._auth)

    @cached_property
    def on_demand_videos(self) -> AsyncOnDemandVideos:
        return AsyncOnDemandVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def payments_essentials(self) -> AsyncPaymentsEssentials:
        return AsyncPaymentsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def portfolios_essentials(self) -> AsyncPortfoliosEssentials:
        return AsyncPortfoliosEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def portfolios_videos(self) -> AsyncPortfoliosVideos:
        return AsyncPortfoliosVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def search_federated(self) -> AsyncSearchFederated:
        return AsyncSearchFederated(self._raw_client, self._server, self._auth)

    @cached_property
    def showcases_custom_showcase_logos(self) -> AsyncShowcasesCustomShowcaseLogos:
        return AsyncShowcasesCustomShowcaseLogos(self._raw_client, self._server, self._auth)

    @cached_property
    def showcases_custom_showcase_thumbnails(self) -> AsyncShowcasesCustomShowcaseThumbnails:
        return AsyncShowcasesCustomShowcaseThumbnails(self._raw_client, self._server, self._auth)

    @cached_property
    def showcases_essentials(self) -> AsyncShowcasesEssentials:
        return AsyncShowcasesEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def showcases_showcase_videos(self) -> AsyncShowcasesShowcaseVideos:
        return AsyncShowcasesShowcaseVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_plans_essentials(self) -> AsyncSubscriptionPlansEssentials:
        return AsyncSubscriptionPlansEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def tags_essentials(self) -> AsyncTagsEssentials:
        return AsyncTagsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def teams_essentials(self) -> AsyncTeamsEssentials:
        return AsyncTeamsEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def teams_members(self) -> AsyncTeamsMembers:
        return AsyncTeamsMembers(self._raw_client, self._server, self._auth)

    @cached_property
    def tutorial_essentials(self) -> AsyncTutorialEssentials:
        return AsyncTutorialEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def users_analytics(self) -> AsyncUsersAnalytics:
        return AsyncUsersAnalytics(self._raw_client, self._server, self._auth)

    @cached_property
    def users_essentials(self) -> AsyncUsersEssentials:
        return AsyncUsersEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def users_feeds(self) -> AsyncUsersFeeds:
        return AsyncUsersFeeds(self._raw_client, self._server, self._auth)

    @cached_property
    def users_followers(self) -> AsyncUsersFollowers:
        return AsyncUsersFollowers(self._raw_client, self._server, self._auth)

    @cached_property
    def users_lms(self) -> AsyncUsersLms:
        return AsyncUsersLms(self._raw_client, self._server, self._auth)

    @cached_property
    def users_pictures(self) -> AsyncUsersPictures:
        return AsyncUsersPictures(self._raw_client, self._server, self._auth)

    @cached_property
    def users_search(self) -> AsyncUsersSearch:
        return AsyncUsersSearch(self._raw_client, self._server, self._auth)

    @cached_property
    def users_watch_history(self) -> AsyncUsersWatchHistory:
        return AsyncUsersWatchHistory(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_ai(self) -> AsyncVideosAi:
        return AsyncVideosAi(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_animated_thumbnails(self) -> AsyncVideosAnimatedThumbnails:
        return AsyncVideosAnimatedThumbnails(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_chapters(self) -> AsyncVideosChapters:
        return AsyncVideosChapters(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_content_ratings(self) -> AsyncVideosContentRatings:
        return AsyncVideosContentRatings(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_creative_commons(self) -> AsyncVideosCreativeCommons:
        return AsyncVideosCreativeCommons(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_credits(self) -> AsyncVideosCredits:
        return AsyncVideosCredits(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_embed_privacy(self) -> AsyncVideosEmbedPrivacy:
        return AsyncVideosEmbedPrivacy(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_essentials(self) -> AsyncVideosEssentials:
        return AsyncVideosEssentials(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_fragments(self) -> AsyncVideosFragments:
        return AsyncVideosFragments(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_languages(self) -> AsyncVideosLanguages:
        return AsyncVideosLanguages(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_live_m3_u8_playback(self) -> AsyncVideosLiveM3U8Playback:
        return AsyncVideosLiveM3U8Playback(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_moderation(self) -> AsyncVideosModeration:
        return AsyncVideosModeration(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_nondestructive_trimming(self) -> AsyncVideosNondestructiveTrimming:
        return AsyncVideosNondestructiveTrimming(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_recommendations(self) -> AsyncVideosRecommendations:
        return AsyncVideosRecommendations(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_showcases(self) -> AsyncVideosShowcases:
        return AsyncVideosShowcases(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_tags(self) -> AsyncVideosTags:
        return AsyncVideosTags(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_text_tracks(self) -> AsyncVideosTextTracks:
        return AsyncVideosTextTracks(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_thumbnails(self) -> AsyncVideosThumbnails:
        return AsyncVideosThumbnails(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_transcripts(self) -> AsyncVideosTranscripts:
        return AsyncVideosTranscripts(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_unlisted_videos(self) -> AsyncVideosUnlistedVideos:
        return AsyncVideosUnlistedVideos(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_uploads(self) -> AsyncVideosUploads:
        return AsyncVideosUploads(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_versions(self) -> AsyncVideosVersions:
        return AsyncVideosVersions(self._raw_client, self._server, self._auth)

    @cached_property
    def videos_video_comments(self) -> AsyncVideosVideoComments:
        return AsyncVideosVideoComments(self._raw_client, self._server, self._auth)

    @cached_property
    def watch_later_queue_essentials(self) -> AsyncWatchLaterQueueEssentials:
        return AsyncWatchLaterQueueEssentials(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncVimeoClient
