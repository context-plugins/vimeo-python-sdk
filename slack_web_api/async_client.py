from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.admin import AsyncAdmin
from .apis.admin_apps import AsyncAdminApps
from .apis.admin_apps_approved import AsyncAdminAppsApproved
from .apis.admin_apps_requests import AsyncAdminAppsRequests
from .apis.admin_apps_restricted import AsyncAdminAppsRestricted
from .apis.admin_conversations import AsyncAdminConversations
from .apis.admin_conversations_ekm import AsyncAdminConversationsEkm
from .apis.admin_conversations_restrict_access import AsyncAdminConversationsRestrictAccess
from .apis.admin_emoji import AsyncAdminEmoji
from .apis.admin_invite_requests import AsyncAdminInviteRequests
from .apis.admin_invite_requests_approved import AsyncAdminInviteRequestsApproved
from .apis.admin_invite_requests_denied import AsyncAdminInviteRequestsDenied
from .apis.admin_teams import AsyncAdminTeams
from .apis.admin_teams_admins import AsyncAdminTeamsAdmins
from .apis.admin_teams_owners import AsyncAdminTeamsOwners
from .apis.admin_teams_settings import AsyncAdminTeamsSettings
from .apis.admin_usergroups import AsyncAdminUsergroups
from .apis.admin_users import AsyncAdminUsers
from .apis.admin_users_session import AsyncAdminUsersSession
from .apis.api2 import AsyncApi2
from .apis.apps import AsyncApps
from .apis.apps_event_authorizations import AsyncAppsEventAuthorizations
from .apis.apps_permissions import AsyncAppsPermissions
from .apis.apps_permissions_resources import AsyncAppsPermissionsResources
from .apis.apps_permissions_scopes import AsyncAppsPermissionsScopes
from .apis.apps_permissions_users import AsyncAppsPermissionsUsers
from .apis.auth_api import AsyncAuthApi
from .apis.bots import AsyncBots
from .apis.calls import AsyncCalls
from .apis.calls_participants import AsyncCallsParticipants
from .apis.chat import AsyncChat
from .apis.chat_scheduled_messages import AsyncChatScheduledMessages
from .apis.conversations import AsyncConversations
from .apis.dialog import AsyncDialog
from .apis.dnd import AsyncDnd
from .apis.emoji import AsyncEmoji
from .apis.files import AsyncFiles
from .apis.files_comments import AsyncFilesComments
from .apis.files_remote import AsyncFilesRemote
from .apis.migration import AsyncMigration
from .apis.oauth import AsyncOauth
from .apis.oauth_v2 import AsyncOauthV2
from .apis.pins import AsyncPins
from .apis.reactions import AsyncReactions
from .apis.reminders import AsyncReminders
from .apis.rtm import AsyncRtm
from .apis.search import AsyncSearch
from .apis.stars import AsyncStars
from .apis.team_api import AsyncTeamApi
from .apis.team_profile import AsyncTeamProfile
from .apis.usergroups import AsyncUsergroups
from .apis.usergroups_users import AsyncUsergroupsUsers
from .apis.users import AsyncUsers
from .apis.users_profile import AsyncUsersProfile
from .apis.views import AsyncViews
from .apis.workflows import AsyncWorkflows
from .auth import AsyncAuthSchemes, SlackAuthScope
from .base_client import DEFAULT_TIMEOUT, BaseSlackWebApiClient
from .core import (
    AsyncAuthorizationCodeCredentials,
    AsyncAuthorizationCodeCredentialsOrDict,
    AsyncAuthorizationCodeTokenSource,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncOAuth2RefreshableScheme,
    AsyncRawClient,
    AsyncRefreshableTokenSource,
    client_secret_basic,
    no_auth,
)
from .server.environment import Environment


class AsyncSlackWebApiClient(BaseSlackWebApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        slack_auth: AsyncAuthorizationCodeCredentialsOrDict[SlackAuthScope] | None = None,
        slack_auth_token_source: (
            AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[SlackAuthScope]] | None
        ) = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
        )
        self._auth = AsyncAuthSchemes(
            slack_auth=(
                AsyncOAuth2RefreshableScheme(
                    credentials=AsyncAuthorizationCodeCredentials[SlackAuthScope].coerce(slack_auth),
                    source=(
                        slack_auth_token_source
                        if slack_auth_token_source is not None
                        else AsyncAuthorizationCodeTokenSource[SlackAuthScope](
                            client=self._raw_client,
                            authorization_url=self._server.default("/authorize"),
                            token_url=self._server.default("/oauth.access"),
                            refresh_url=self._server.default("/oauth.access"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if slack_auth is not None
                else no_auth
            ),
        )

    @cached_property
    def admin(self) -> AsyncAdmin:
        return AsyncAdmin(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_apps(self) -> AsyncAdminApps:
        return AsyncAdminApps(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_apps_approved(self) -> AsyncAdminAppsApproved:
        return AsyncAdminAppsApproved(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_apps_requests(self) -> AsyncAdminAppsRequests:
        return AsyncAdminAppsRequests(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_apps_restricted(self) -> AsyncAdminAppsRestricted:
        return AsyncAdminAppsRestricted(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_conversations(self) -> AsyncAdminConversations:
        return AsyncAdminConversations(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_conversations_ekm(self) -> AsyncAdminConversationsEkm:
        return AsyncAdminConversationsEkm(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_conversations_restrict_access(self) -> AsyncAdminConversationsRestrictAccess:
        return AsyncAdminConversationsRestrictAccess(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_emoji(self) -> AsyncAdminEmoji:
        return AsyncAdminEmoji(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_invite_requests(self) -> AsyncAdminInviteRequests:
        return AsyncAdminInviteRequests(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_invite_requests_approved(self) -> AsyncAdminInviteRequestsApproved:
        return AsyncAdminInviteRequestsApproved(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_invite_requests_denied(self) -> AsyncAdminInviteRequestsDenied:
        return AsyncAdminInviteRequestsDenied(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_teams(self) -> AsyncAdminTeams:
        return AsyncAdminTeams(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_teams_admins(self) -> AsyncAdminTeamsAdmins:
        return AsyncAdminTeamsAdmins(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_teams_owners(self) -> AsyncAdminTeamsOwners:
        return AsyncAdminTeamsOwners(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_teams_settings(self) -> AsyncAdminTeamsSettings:
        return AsyncAdminTeamsSettings(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_usergroups(self) -> AsyncAdminUsergroups:
        return AsyncAdminUsergroups(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_users(self) -> AsyncAdminUsers:
        return AsyncAdminUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_users_session(self) -> AsyncAdminUsersSession:
        return AsyncAdminUsersSession(self._raw_client, self._server, self._auth)

    @cached_property
    def api2(self) -> AsyncApi2:
        return AsyncApi2(self._raw_client, self._server, self._auth)

    @cached_property
    def apps(self) -> AsyncApps:
        return AsyncApps(self._raw_client, self._server, self._auth)

    @cached_property
    def apps_event_authorizations(self) -> AsyncAppsEventAuthorizations:
        return AsyncAppsEventAuthorizations(self._raw_client, self._server, self._auth)

    @cached_property
    def apps_permissions(self) -> AsyncAppsPermissions:
        return AsyncAppsPermissions(self._raw_client, self._server, self._auth)

    @cached_property
    def apps_permissions_resources(self) -> AsyncAppsPermissionsResources:
        return AsyncAppsPermissionsResources(self._raw_client, self._server, self._auth)

    @cached_property
    def apps_permissions_scopes(self) -> AsyncAppsPermissionsScopes:
        return AsyncAppsPermissionsScopes(self._raw_client, self._server, self._auth)

    @cached_property
    def apps_permissions_users(self) -> AsyncAppsPermissionsUsers:
        return AsyncAppsPermissionsUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def auth_api(self) -> AsyncAuthApi:
        return AsyncAuthApi(self._raw_client, self._server, self._auth)

    @cached_property
    def bots(self) -> AsyncBots:
        return AsyncBots(self._raw_client, self._server, self._auth)

    @cached_property
    def calls(self) -> AsyncCalls:
        return AsyncCalls(self._raw_client, self._server, self._auth)

    @cached_property
    def calls_participants(self) -> AsyncCallsParticipants:
        return AsyncCallsParticipants(self._raw_client, self._server, self._auth)

    @cached_property
    def chat(self) -> AsyncChat:
        return AsyncChat(self._raw_client, self._server, self._auth)

    @cached_property
    def chat_scheduled_messages(self) -> AsyncChatScheduledMessages:
        return AsyncChatScheduledMessages(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations(self) -> AsyncConversations:
        return AsyncConversations(self._raw_client, self._server, self._auth)

    @cached_property
    def dialog(self) -> AsyncDialog:
        return AsyncDialog(self._raw_client, self._server, self._auth)

    @cached_property
    def dnd(self) -> AsyncDnd:
        return AsyncDnd(self._raw_client, self._server, self._auth)

    @cached_property
    def emoji(self) -> AsyncEmoji:
        return AsyncEmoji(self._raw_client, self._server, self._auth)

    @cached_property
    def files(self) -> AsyncFiles:
        return AsyncFiles(self._raw_client, self._server, self._auth)

    @cached_property
    def files_comments(self) -> AsyncFilesComments:
        return AsyncFilesComments(self._raw_client, self._server, self._auth)

    @cached_property
    def files_remote(self) -> AsyncFilesRemote:
        return AsyncFilesRemote(self._raw_client, self._server, self._auth)

    @cached_property
    def migration(self) -> AsyncMigration:
        return AsyncMigration(self._raw_client, self._server, self._auth)

    @cached_property
    def oauth(self) -> AsyncOauth:
        return AsyncOauth(self._raw_client, self._server, self._auth)

    @cached_property
    def oauth_v2(self) -> AsyncOauthV2:
        return AsyncOauthV2(self._raw_client, self._server, self._auth)

    @cached_property
    def pins(self) -> AsyncPins:
        return AsyncPins(self._raw_client, self._server, self._auth)

    @cached_property
    def reactions(self) -> AsyncReactions:
        return AsyncReactions(self._raw_client, self._server, self._auth)

    @cached_property
    def reminders(self) -> AsyncReminders:
        return AsyncReminders(self._raw_client, self._server, self._auth)

    @cached_property
    def rtm(self) -> AsyncRtm:
        return AsyncRtm(self._raw_client, self._server, self._auth)

    @cached_property
    def search(self) -> AsyncSearch:
        return AsyncSearch(self._raw_client, self._server, self._auth)

    @cached_property
    def stars(self) -> AsyncStars:
        return AsyncStars(self._raw_client, self._server, self._auth)

    @cached_property
    def team_api(self) -> AsyncTeamApi:
        return AsyncTeamApi(self._raw_client, self._server, self._auth)

    @cached_property
    def team_profile(self) -> AsyncTeamProfile:
        return AsyncTeamProfile(self._raw_client, self._server, self._auth)

    @cached_property
    def usergroups(self) -> AsyncUsergroups:
        return AsyncUsergroups(self._raw_client, self._server, self._auth)

    @cached_property
    def usergroups_users(self) -> AsyncUsergroupsUsers:
        return AsyncUsergroupsUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def users(self) -> AsyncUsers:
        return AsyncUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def users_profile(self) -> AsyncUsersProfile:
        return AsyncUsersProfile(self._raw_client, self._server, self._auth)

    @cached_property
    def views(self) -> AsyncViews:
        return AsyncViews(self._raw_client, self._server, self._auth)

    @cached_property
    def workflows(self) -> AsyncWorkflows:
        return AsyncWorkflows(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncSlackWebApiClient
