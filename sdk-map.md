<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Slack Web API (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Slack Web API |
| Root package | `slack_web_api` |
| Distribution name | `slack-web-api` |
| Requires | Python 3.10 or later |
| API spec version | `1.7.0` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from slack_web_api import SlackWebApiClient
from slack_web_api.auth import SlackAuthScope
from slack_web_api.core import AuthorizationCodeCredentials


def prompt(url: str) -> str:
    return input(f"Open {url}, then paste the code: ")


client = SlackWebApiClient(
    slack_auth=AuthorizationCodeCredentials[SlackAuthScope](
        client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
    ),
    environment="production",
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with SlackWebApiClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run, to_thread

from slack_web_api import AsyncSlackWebApiClient
from slack_web_api.auth import SlackAuthScope
from slack_web_api.core import AsyncAuthorizationCodeCredentials


async def prompt(url: str) -> str:
    print(f"Open {url}")
    return await to_thread(input, "Paste the code: ")


async def main() -> None:
    client = AsyncSlackWebApiClient(
        slack_auth=AsyncAuthorizationCodeCredentials[SlackAuthScope](
            client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
        ),
        environment="production",
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncSlackWebApiClient(...) as client:` closes the pool on exit.

`AsyncClient` (`slack_web_api/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `SlackWebApiClient` and `AsyncSlackWebApiClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.admin`). Every constructor argument is optional and keyword-only. Sources: `slack_web_api/client.py`, `slack_web_api/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `environment` | `Environment` | `Environment` | `"production"` |
| `base_url` | `str \| None` | `str \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `slack_auth` | `AuthorizationCodeCredentialsOrDict[SlackAuthScope] \| None` | `AsyncAuthorizationCodeCredentialsOrDict[SlackAuthScope] \| None` | `None` |
| `slack_auth_token_source` | `RefreshableTokenSource[AuthorizationCodeCredentials[SlackAuthScope]] \| None` | `AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[SlackAuthScope]] \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `Environment` | `slack_web_api.server` | `Literal` of the Environments table's names |
| `HttpClient` | `slack_web_api.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()` |
| `AuthorizationCodeCredentialsOrDict` | `slack_web_api.core` | `AuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `SlackAuthScope` | `slack_web_api.auth` | `Enum` of the declared scopes |
| `RefreshableTokenSource` | `slack_web_api.core` | protocol — `fetch(credentials) -> OAuthTokenRefreshable` · `refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AuthorizationCodeCredentials` | `slack_web_api.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `AsyncHttpClient` | `slack_web_api.core` | protocol — `async send(request: HttpRequest) -> HttpResponse` · `async aclose()` |
| `AsyncAuthorizationCodeCredentialsOrDict` | `slack_web_api.core` | `AsyncAuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncRefreshableTokenSource` | `slack_web_api.core` | protocol — `async fetch(credentials) -> OAuthTokenRefreshable` · `async refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AsyncAuthorizationCodeCredentials` | `slack_web_api.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.response`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `slack_web_api/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`slack_web_api/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse`.

Core runtime types (`slack_web_api/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is always `RawError` (no Case A alias in this SDK) | `error: E` · `status_code: int` · `response: HttpResponse` | `slack_web_api/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `response: HttpResponse` (on both) | `slack_web_api/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse` | `slack_web_api/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
from slack_web_api.core import ApiError, RawError

try:
    response = client.admin.admin_apps_approve(token, content_type)
except ApiError as e:
    # Case B — raw error: e.error is RawError
    print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **253 operations**, **0 are Case A (typed)** and **253 are Case B (raw)**.

---

## Operations — by controller (56 pages, 253 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every type it names, with the module that declares it.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout or extra headers; every signature ends with it | here (`slack_web_api/core/request_options.py`) |
| **Base URL is the selected environment's** — this SDK's only server, one URL per `environment=`; override it with `base_url="https://…"` | Servers & auth |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.admin` | 56 | [map/operations/admin.md](map/operations/admin.md) |
| `client.admin_apps` | 2 | [map/operations/admin_apps.md](map/operations/admin_apps.md) |
| `client.admin_apps_approved` | 1 | [map/operations/admin_apps_approved.md](map/operations/admin_apps_approved.md) |
| `client.admin_apps_requests` | 1 | [map/operations/admin_apps_requests.md](map/operations/admin_apps_requests.md) |
| `client.admin_apps_restricted` | 1 | [map/operations/admin_apps_restricted.md](map/operations/admin_apps_restricted.md) |
| `client.admin_conversations` | 13 | [map/operations/admin_conversations.md](map/operations/admin_conversations.md) |
| `client.admin_conversations_ekm` | 1 | [map/operations/admin_conversations_ekm.md](map/operations/admin_conversations_ekm.md) |
| `client.admin_conversations_restrict_access` | 3 | [map/operations/admin_conversations_restrict_access.md](map/operations/admin_conversations_restrict_access.md) |
| `client.admin_emoji` | 5 | [map/operations/admin_emoji.md](map/operations/admin_emoji.md) |
| `client.admin_invite_requests` | 3 | [map/operations/admin_invite_requests.md](map/operations/admin_invite_requests.md) |
| `client.admin_invite_requests_approved` | 1 | [map/operations/admin_invite_requests_approved.md](map/operations/admin_invite_requests_approved.md) |
| `client.admin_invite_requests_denied` | 1 | [map/operations/admin_invite_requests_denied.md](map/operations/admin_invite_requests_denied.md) |
| `client.admin_teams` | 2 | [map/operations/admin_teams.md](map/operations/admin_teams.md) |
| `client.admin_teams_admins` | 1 | [map/operations/admin_teams_admins.md](map/operations/admin_teams_admins.md) |
| `client.admin_teams_owners` | 1 | [map/operations/admin_teams_owners.md](map/operations/admin_teams_owners.md) |
| `client.admin_teams_settings` | 6 | [map/operations/admin_teams_settings.md](map/operations/admin_teams_settings.md) |
| `client.admin_usergroups` | 4 | [map/operations/admin_usergroups.md](map/operations/admin_usergroups.md) |
| `client.admin_users` | 8 | [map/operations/admin_users.md](map/operations/admin_users.md) |
| `client.admin_users_session` | 2 | [map/operations/admin_users_session.md](map/operations/admin_users_session.md) |
| `client.api2` | 1 | [map/operations/api2.md](map/operations/api2.md) |
| `client.apps` | 8 | [map/operations/apps.md](map/operations/apps.md) |
| `client.apps_event_authorizations` | 1 | [map/operations/apps_event_authorizations.md](map/operations/apps_event_authorizations.md) |
| `client.apps_permissions` | 2 | [map/operations/apps_permissions.md](map/operations/apps_permissions.md) |
| `client.apps_permissions_resources` | 1 | [map/operations/apps_permissions_resources.md](map/operations/apps_permissions_resources.md) |
| `client.apps_permissions_scopes` | 1 | [map/operations/apps_permissions_scopes.md](map/operations/apps_permissions_scopes.md) |
| `client.apps_permissions_users` | 2 | [map/operations/apps_permissions_users.md](map/operations/apps_permissions_users.md) |
| `client.auth_api` | 2 | [map/operations/auth_api.md](map/operations/auth_api.md) |
| `client.bots` | 1 | [map/operations/bots.md](map/operations/bots.md) |
| `client.calls` | 6 | [map/operations/calls.md](map/operations/calls.md) |
| `client.calls_participants` | 2 | [map/operations/calls_participants.md](map/operations/calls_participants.md) |
| `client.chat` | 10 | [map/operations/chat.md](map/operations/chat.md) |
| `client.chat_scheduled_messages` | 1 | [map/operations/chat_scheduled_messages.md](map/operations/chat_scheduled_messages.md) |
| `client.conversations` | 18 | [map/operations/conversations.md](map/operations/conversations.md) |
| `client.dialog` | 1 | [map/operations/dialog.md](map/operations/dialog.md) |
| `client.dnd` | 5 | [map/operations/dnd.md](map/operations/dnd.md) |
| `client.emoji` | 1 | [map/operations/emoji.md](map/operations/emoji.md) |
| `client.files` | 13 | [map/operations/files.md](map/operations/files.md) |
| `client.files_comments` | 1 | [map/operations/files_comments.md](map/operations/files_comments.md) |
| `client.files_remote` | 6 | [map/operations/files_remote.md](map/operations/files_remote.md) |
| `client.migration` | 1 | [map/operations/migration.md](map/operations/migration.md) |
| `client.oauth` | 3 | [map/operations/oauth.md](map/operations/oauth.md) |
| `client.oauth_v2` | 1 | [map/operations/oauth_v2.md](map/operations/oauth_v2.md) |
| `client.pins` | 3 | [map/operations/pins.md](map/operations/pins.md) |
| `client.reactions` | 4 | [map/operations/reactions.md](map/operations/reactions.md) |
| `client.reminders` | 5 | [map/operations/reminders.md](map/operations/reminders.md) |
| `client.rtm` | 1 | [map/operations/rtm.md](map/operations/rtm.md) |
| `client.search` | 1 | [map/operations/search.md](map/operations/search.md) |
| `client.stars` | 3 | [map/operations/stars.md](map/operations/stars.md) |
| `client.team_api` | 5 | [map/operations/team_api.md](map/operations/team_api.md) |
| `client.team_profile` | 1 | [map/operations/team_profile.md](map/operations/team_profile.md) |
| `client.usergroups` | 7 | [map/operations/usergroups.md](map/operations/usergroups.md) |
| `client.usergroups_users` | 2 | [map/operations/usergroups_users.md](map/operations/usergroups_users.md) |
| `client.users` | 12 | [map/operations/users.md](map/operations/users.md) |
| `client.users_profile` | 2 | [map/operations/users_profile.md](map/operations/users_profile.md) |
| `client.views` | 4 | [map/operations/views.md](map/operations/views.md) |
| `client.workflows` | 3 | [map/operations/workflows.md](map/operations/workflows.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `slack_web_api/models/` declares one type plus its input companion, and every module under `slack_web_api/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`ApimethodusersGetPresence` ↔ `apimethodusers_get_presence.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 357 | `slack_web_api/models/` |
| Enums (`Enum` over `str`) — Python member names + wire values | 89 | `slack_web_api/models/enums/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`type_` ↔ `"type"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model and enum also has an **input companion**, exported beside it from the same package (`ApimethodusersGetPresence` ↔ `ApimethodusersGetPresenceDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AdminConversationsArchiveErrorEnum` ↔ `AdminConversationsArchiveErrorEnumOrStr`) and additionally accepts a wire value this SDK version does not know.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `slack_web_api` |
| Operation controllers | `slack_web_api.apis` |
| Models | `slack_web_api.models` |
| Enums | `slack_web_api.models.enums` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `slack_web_api.core` |

---

## Servers & auth

**OAuth2 (authorization code).** Pass `slack_auth` your client id, redirect URI and authorization code; authorization is at `/authorize` and tokens come from `/oauth.access`, both on the base URL — so `base_url="https://…"` moves token traffic too. Scopes are the `SlackAuthScope` alias.

**Environments.** `environment=` selects the target environment (`slack_web_api/server/environment.py`); this SDK's one server (`slack_web_api/server/server_config.py`) has a base URL per environment:

| Environment | Base URL | Hosting | Override point |
| --- | --- | --- | --- |
| `"production"` *(default)* | `https://slack.com/api` | — | `base_url="https://…"` |
| `"environment2"` | `https://slack.com/oauth` | — | `base_url="https://…"` |

Pick a row with `environment=`.

