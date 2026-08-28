from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.admin import Admin
from .apis.admin_apps import AdminApps
from .apis.admin_apps_approved import AdminAppsApproved
from .apis.admin_apps_requests import AdminAppsRequests
from .apis.admin_apps_restricted import AdminAppsRestricted
from .apis.admin_conversations import AdminConversations
from .apis.admin_conversations_ekm import AdminConversationsEkm
from .apis.admin_conversations_restrict_access import AdminConversationsRestrictAccess
from .apis.admin_emoji import AdminEmoji
from .apis.admin_invite_requests import AdminInviteRequests
from .apis.admin_invite_requests_approved import AdminInviteRequestsApproved
from .apis.admin_invite_requests_denied import AdminInviteRequestsDenied
from .apis.admin_teams import AdminTeams
from .apis.admin_teams_admins import AdminTeamsAdmins
from .apis.admin_teams_owners import AdminTeamsOwners
from .apis.admin_teams_settings import AdminTeamsSettings
from .apis.admin_usergroups import AdminUsergroups
from .apis.admin_users import AdminUsers
from .apis.admin_users_session import AdminUsersSession
from .apis.api2 import Api2
from .apis.apps import Apps
from .apis.apps_event_authorizations import AppsEventAuthorizations
from .apis.apps_permissions import AppsPermissions
from .apis.apps_permissions_resources import AppsPermissionsResources
from .apis.apps_permissions_scopes import AppsPermissionsScopes
from .apis.apps_permissions_users import AppsPermissionsUsers
from .apis.auth_api import AuthApi
from .apis.bots import Bots
from .apis.calls import Calls
from .apis.calls_participants import CallsParticipants
from .apis.chat import Chat
from .apis.chat_scheduled_messages import ChatScheduledMessages
from .apis.conversations import Conversations
from .apis.dialog import Dialog
from .apis.dnd import Dnd
from .apis.emoji import Emoji
from .apis.files import Files
from .apis.files_comments import FilesComments
from .apis.files_remote import FilesRemote
from .apis.migration import Migration
from .apis.oauth import Oauth
from .apis.oauth_v2 import OauthV2
from .apis.pins import Pins
from .apis.reactions import Reactions
from .apis.reminders import Reminders
from .apis.rtm import Rtm
from .apis.search import Search
from .apis.stars import Stars
from .apis.team_api import TeamApi
from .apis.team_profile import TeamProfile
from .apis.usergroups import Usergroups
from .apis.usergroups_users import UsergroupsUsers
from .apis.users import Users
from .apis.users_profile import UsersProfile
from .apis.views import Views
from .apis.workflows import Workflows
from .auth import AuthSchemes, SlackAuthScope
from .base_client import DEFAULT_TIMEOUT, BaseSlackWebApiClient
from .core import (
    AuthorizationCodeCredentials,
    AuthorizationCodeCredentialsOrDict,
    AuthorizationCodeTokenSource,
    HttpClient,
    HttpxClient,
    OAuth2RefreshableScheme,
    RawClient,
    RefreshableTokenSource,
    client_secret_basic,
    no_auth,
)
from .server.environment import Environment


class SlackWebApiClient(BaseSlackWebApiClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        slack_auth: AuthorizationCodeCredentialsOrDict[SlackAuthScope] | None = None,
        slack_auth_token_source: RefreshableTokenSource[AuthorizationCodeCredentials[SlackAuthScope]] | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout)
        )
        self._auth = AuthSchemes(
            slack_auth=(
                OAuth2RefreshableScheme(
                    credentials=AuthorizationCodeCredentials[SlackAuthScope].coerce(slack_auth),
                    source=(
                        slack_auth_token_source
                        if slack_auth_token_source is not None
                        else AuthorizationCodeTokenSource[SlackAuthScope](
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
    def admin(self) -> Admin:
        return Admin(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_apps(self) -> AdminApps:
        return AdminApps(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_apps_approved(self) -> AdminAppsApproved:
        return AdminAppsApproved(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_apps_requests(self) -> AdminAppsRequests:
        return AdminAppsRequests(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_apps_restricted(self) -> AdminAppsRestricted:
        return AdminAppsRestricted(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_conversations(self) -> AdminConversations:
        return AdminConversations(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_conversations_ekm(self) -> AdminConversationsEkm:
        return AdminConversationsEkm(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_conversations_restrict_access(self) -> AdminConversationsRestrictAccess:
        return AdminConversationsRestrictAccess(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_emoji(self) -> AdminEmoji:
        return AdminEmoji(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_invite_requests(self) -> AdminInviteRequests:
        return AdminInviteRequests(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_invite_requests_approved(self) -> AdminInviteRequestsApproved:
        return AdminInviteRequestsApproved(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_invite_requests_denied(self) -> AdminInviteRequestsDenied:
        return AdminInviteRequestsDenied(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_teams(self) -> AdminTeams:
        return AdminTeams(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_teams_admins(self) -> AdminTeamsAdmins:
        return AdminTeamsAdmins(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_teams_owners(self) -> AdminTeamsOwners:
        return AdminTeamsOwners(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_teams_settings(self) -> AdminTeamsSettings:
        return AdminTeamsSettings(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_usergroups(self) -> AdminUsergroups:
        return AdminUsergroups(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_users(self) -> AdminUsers:
        return AdminUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def admin_users_session(self) -> AdminUsersSession:
        return AdminUsersSession(self._raw_client, self._server, self._auth)

    @cached_property
    def api2(self) -> Api2:
        return Api2(self._raw_client, self._server, self._auth)

    @cached_property
    def apps(self) -> Apps:
        return Apps(self._raw_client, self._server, self._auth)

    @cached_property
    def apps_event_authorizations(self) -> AppsEventAuthorizations:
        return AppsEventAuthorizations(self._raw_client, self._server, self._auth)

    @cached_property
    def apps_permissions(self) -> AppsPermissions:
        return AppsPermissions(self._raw_client, self._server, self._auth)

    @cached_property
    def apps_permissions_resources(self) -> AppsPermissionsResources:
        return AppsPermissionsResources(self._raw_client, self._server, self._auth)

    @cached_property
    def apps_permissions_scopes(self) -> AppsPermissionsScopes:
        return AppsPermissionsScopes(self._raw_client, self._server, self._auth)

    @cached_property
    def apps_permissions_users(self) -> AppsPermissionsUsers:
        return AppsPermissionsUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def auth_api(self) -> AuthApi:
        return AuthApi(self._raw_client, self._server, self._auth)

    @cached_property
    def bots(self) -> Bots:
        return Bots(self._raw_client, self._server, self._auth)

    @cached_property
    def calls(self) -> Calls:
        return Calls(self._raw_client, self._server, self._auth)

    @cached_property
    def calls_participants(self) -> CallsParticipants:
        return CallsParticipants(self._raw_client, self._server, self._auth)

    @cached_property
    def chat(self) -> Chat:
        return Chat(self._raw_client, self._server, self._auth)

    @cached_property
    def chat_scheduled_messages(self) -> ChatScheduledMessages:
        return ChatScheduledMessages(self._raw_client, self._server, self._auth)

    @cached_property
    def conversations(self) -> Conversations:
        return Conversations(self._raw_client, self._server, self._auth)

    @cached_property
    def dialog(self) -> Dialog:
        return Dialog(self._raw_client, self._server, self._auth)

    @cached_property
    def dnd(self) -> Dnd:
        return Dnd(self._raw_client, self._server, self._auth)

    @cached_property
    def emoji(self) -> Emoji:
        return Emoji(self._raw_client, self._server, self._auth)

    @cached_property
    def files(self) -> Files:
        return Files(self._raw_client, self._server, self._auth)

    @cached_property
    def files_comments(self) -> FilesComments:
        return FilesComments(self._raw_client, self._server, self._auth)

    @cached_property
    def files_remote(self) -> FilesRemote:
        return FilesRemote(self._raw_client, self._server, self._auth)

    @cached_property
    def migration(self) -> Migration:
        return Migration(self._raw_client, self._server, self._auth)

    @cached_property
    def oauth(self) -> Oauth:
        return Oauth(self._raw_client, self._server, self._auth)

    @cached_property
    def oauth_v2(self) -> OauthV2:
        return OauthV2(self._raw_client, self._server, self._auth)

    @cached_property
    def pins(self) -> Pins:
        return Pins(self._raw_client, self._server, self._auth)

    @cached_property
    def reactions(self) -> Reactions:
        return Reactions(self._raw_client, self._server, self._auth)

    @cached_property
    def reminders(self) -> Reminders:
        return Reminders(self._raw_client, self._server, self._auth)

    @cached_property
    def rtm(self) -> Rtm:
        return Rtm(self._raw_client, self._server, self._auth)

    @cached_property
    def search(self) -> Search:
        return Search(self._raw_client, self._server, self._auth)

    @cached_property
    def stars(self) -> Stars:
        return Stars(self._raw_client, self._server, self._auth)

    @cached_property
    def team_api(self) -> TeamApi:
        return TeamApi(self._raw_client, self._server, self._auth)

    @cached_property
    def team_profile(self) -> TeamProfile:
        return TeamProfile(self._raw_client, self._server, self._auth)

    @cached_property
    def usergroups(self) -> Usergroups:
        return Usergroups(self._raw_client, self._server, self._auth)

    @cached_property
    def usergroups_users(self) -> UsergroupsUsers:
        return UsergroupsUsers(self._raw_client, self._server, self._auth)

    @cached_property
    def users(self) -> Users:
        return Users(self._raw_client, self._server, self._auth)

    @cached_property
    def users_profile(self) -> UsersProfile:
        return UsersProfile(self._raw_client, self._server, self._auth)

    @cached_property
    def views(self) -> Views:
        return Views(self._raw_client, self._server, self._auth)

    @cached_property
    def workflows(self) -> Workflows:
        return Workflows(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = SlackWebApiClient
