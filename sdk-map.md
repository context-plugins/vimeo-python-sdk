<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Vimeo (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Vimeo |
| Root package | `vimeo` |
| Distribution name | `vimeo` |
| Requires | Python 3.10 or later |
| API spec version | `3.4.9` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from vimeo import VimeoClient
from vimeo.auth import Oauth2AuthorizationCodeScope, Oauth2ClientCredentialsScope
from vimeo.core import AuthorizationCodeCredentials, ClientCredentials


def prompt(url: str) -> str:
    return input(f"Open {url}, then paste the code: ")


client = VimeoClient(
    bearer="YOUR_BEARER_TOKEN",
    oauth2_authorization_code=AuthorizationCodeCredentials[Oauth2AuthorizationCodeScope](
        client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
    ),
    oauth2_client_credentials=ClientCredentials[Oauth2ClientCredentialsScope](
        client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"
    ),
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with VimeoClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run, to_thread

from vimeo import AsyncVimeoClient
from vimeo.auth import Oauth2AuthorizationCodeScope, Oauth2ClientCredentialsScope
from vimeo.core import AsyncAuthorizationCodeCredentials, ClientCredentials


async def prompt(url: str) -> str:
    print(f"Open {url}")
    return await to_thread(input, "Paste the code: ")


async def main() -> None:
    client = AsyncVimeoClient(
        bearer="YOUR_BEARER_TOKEN",
        oauth2_authorization_code=AsyncAuthorizationCodeCredentials[Oauth2AuthorizationCodeScope](
            client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
        ),
        oauth2_client_credentials=ClientCredentials[Oauth2ClientCredentialsScope](
            client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"
        ),
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncVimeoClient(...) as client:` closes the pool on exit.

`AsyncClient` (`vimeo/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `VimeoClient` and `AsyncVimeoClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.api_apps_webhooks`). Every constructor argument is optional and keyword-only. Sources: `vimeo/client.py`, `vimeo/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `base_url` | `str \| None` | `str \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `bearer` | `str \| None` | `str \| None` | `None` |
| `oauth2_authorization_code` | `AuthorizationCodeCredentialsOrDict[Oauth2AuthorizationCodeScope] \| None` | `AsyncAuthorizationCodeCredentialsOrDict[Oauth2AuthorizationCodeScope] \| None` | `None` |
| `oauth2_authorization_code_token_source` | `RefreshableTokenSource[AuthorizationCodeCredentials[Oauth2AuthorizationCodeScope]] \| None` | `AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[Oauth2AuthorizationCodeScope]] \| None` | `None` |
| `oauth2_client_credentials` | `ClientCredentialsOrDict[Oauth2ClientCredentialsScope] \| None` | `ClientCredentialsOrDict[Oauth2ClientCredentialsScope] \| None` | `None` |
| `oauth2_client_credentials_token_source` | `TokenSource[ClientCredentials[Oauth2ClientCredentialsScope]] \| None` | `AsyncTokenSource[ClientCredentials[Oauth2ClientCredentialsScope]] \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `HttpClient` | `vimeo.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()` |
| `AuthorizationCodeCredentialsOrDict` | `vimeo.core` | `AuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `Oauth2AuthorizationCodeScope` | `vimeo.auth` | `Enum` of the declared scopes |
| `RefreshableTokenSource` | `vimeo.core` | protocol — `fetch(credentials) -> OAuthTokenRefreshable` · `refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AuthorizationCodeCredentials` | `vimeo.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `ClientCredentialsOrDict` | `vimeo.core` | `ClientCredentials` or a dict: `client_id: str` · `client_secret: str` · `scopes: list[Scope] \| None` |
| `Oauth2ClientCredentialsScope` | `vimeo.auth` | `Enum` of the declared scopes |
| `TokenSource` | `vimeo.core` | protocol — `fetch(credentials) -> OAuthToken` |
| `ClientCredentials` | `vimeo.core` | `client_id: str` · `client_secret: str` · `scopes: list[Scope] \| None` |
| `AsyncHttpClient` | `vimeo.core` | protocol — `async send(request: HttpRequest) -> HttpResponse` · `async aclose()` |
| `AsyncAuthorizationCodeCredentialsOrDict` | `vimeo.core` | `AsyncAuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncRefreshableTokenSource` | `vimeo.core` | protocol — `async fetch(credentials) -> OAuthTokenRefreshable` · `async refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AsyncAuthorizationCodeCredentials` | `vimeo.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncTokenSource` | `vimeo.core` | protocol — `async fetch(credentials) -> OAuthToken` |

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.response`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `vimeo/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`vimeo/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse`.

Core runtime types (`vimeo/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `vimeo/errors/` or `RawError` | `error: E` · `status_code: int` · `response: HttpResponse` | `vimeo/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `response: HttpResponse` (on both) | `vimeo/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse` | `vimeo/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
from vimeo.core import ApiError, RawError
from vimeo.models import Error

try:
    response = client.api_apps_webhooks.add_webhook(app_id)
except ApiError as e:
    # Case A — typed error: e.error is AddWebhookErrorBody
    if isinstance(e.error, Error):
        # Handle 400
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **520 operations**, **411 are Case A (typed)** and **109 are Case B (raw)**.

---

## Operations — by controller (100 pages, 520 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every type it names, with the module that declares it.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout or extra headers; every signature ends with it | here (`vimeo/core/request_options.py`) |
| **Base URL `https://api.vimeo.com`** — this SDK's only server; override it with `base_url="https://…"` | Servers & auth |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.api_apps_webhooks` | 5 | [map/operations/api_apps_webhooks.md](map/operations/api_apps_webhooks.md) |
| `client.api_information_essentials` | 1 | [map/operations/api_information_essentials.md](map/operations/api_information_essentials.md) |
| `client.authentication_extras_authenticate` | 1 | [map/operations/authentication_extras_authenticate.md](map/operations/authentication_extras_authenticate.md) |
| `client.authentication_extras_convert` | 1 | [map/operations/authentication_extras_convert.md](map/operations/authentication_extras_convert.md) |
| `client.authentication_extras_essentials` | 2 | [map/operations/authentication_extras_essentials.md](map/operations/authentication_extras_essentials.md) |
| `client.authentication_extras_exchange` | 1 | [map/operations/authentication_extras_exchange.md](map/operations/authentication_extras_exchange.md) |
| `client.categories_channels` | 1 | [map/operations/categories_channels.md](map/operations/categories_channels.md) |
| `client.categories_essentials` | 2 | [map/operations/categories_essentials.md](map/operations/categories_essentials.md) |
| `client.categories_groups` | 1 | [map/operations/categories_groups.md](map/operations/categories_groups.md) |
| `client.categories_users` | 8 | [map/operations/categories_users.md](map/operations/categories_users.md) |
| `client.categories_videos` | 4 | [map/operations/categories_videos.md](map/operations/categories_videos.md) |
| `client.channels_categories` | 4 | [map/operations/channels_categories.md](map/operations/channels_categories.md) |
| `client.channels_essentials` | 7 | [map/operations/channels_essentials.md](map/operations/channels_essentials.md) |
| `client.channels_moderators` | 7 | [map/operations/channels_moderators.md](map/operations/channels_moderators.md) |
| `client.channels_private_channel_members` | 4 | [map/operations/channels_private_channel_members.md](map/operations/channels_private_channel_members.md) |
| `client.channels_subscriptions_and_subscribers` | 7 | [map/operations/channels_subscriptions_and_subscribers.md](map/operations/channels_subscriptions_and_subscribers.md) |
| `client.channels_tags` | 5 | [map/operations/channels_tags.md](map/operations/channels_tags.md) |
| `client.channels_videos` | 7 | [map/operations/channels_videos.md](map/operations/channels_videos.md) |
| `client.embed_presets_custom_logos` | 8 | [map/operations/embed_presets_custom_logos.md](map/operations/embed_presets_custom_logos.md) |
| `client.embed_presets_essentials` | 10 | [map/operations/embed_presets_essentials.md](map/operations/embed_presets_essentials.md) |
| `client.embed_presets_folders` | 1 | [map/operations/embed_presets_folders.md](map/operations/embed_presets_folders.md) |
| `client.embed_presets_timeline_events` | 2 | [map/operations/embed_presets_timeline_events.md](map/operations/embed_presets_timeline_events.md) |
| `client.embed_presets_videos` | 5 | [map/operations/embed_presets_videos.md](map/operations/embed_presets_videos.md) |
| `client.folders_essentials` | 11 | [map/operations/folders_essentials.md](map/operations/folders_essentials.md) |
| `client.folders_items` | 3 | [map/operations/folders_items.md](map/operations/folders_items.md) |
| `client.folders_videos` | 10 | [map/operations/folders_videos.md](map/operations/folders_videos.md) |
| `client.groups_essentials` | 4 | [map/operations/groups_essentials.md](map/operations/groups_essentials.md) |
| `client.groups_subscriptions` | 4 | [map/operations/groups_subscriptions.md](map/operations/groups_subscriptions.md) |
| `client.groups_users` | 5 | [map/operations/groups_users.md](map/operations/groups_users.md) |
| `client.groups_videos` | 5 | [map/operations/groups_videos.md](map/operations/groups_videos.md) |
| `client.likes_essentials` | 11 | [map/operations/likes_essentials.md](map/operations/likes_essentials.md) |
| `client.live_analytics` | 1 | [map/operations/live_analytics.md](map/operations/live_analytics.md) |
| `client.live_audio_tracks` | 2 | [map/operations/live_audio_tracks.md](map/operations/live_audio_tracks.md) |
| `client.live_embed_privacy` | 6 | [map/operations/live_embed_privacy.md](map/operations/live_embed_privacy.md) |
| `client.live_essentials` | 19 | [map/operations/live_essentials.md](map/operations/live_essentials.md) |
| `client.live_event_m3_u8_playback` | 2 | [map/operations/live_event_m3_u8_playback.md](map/operations/live_event_m3_u8_playback.md) |
| `client.live_event_activation` | 3 | [map/operations/live_event_activation.md](map/operations/live_event_activation.md) |
| `client.live_event_automated_closed_captions` | 3 | [map/operations/live_event_automated_closed_captions.md](map/operations/live_event_automated_closed_captions.md) |
| `client.live_event_destinations` | 12 | [map/operations/live_event_destinations.md](map/operations/live_event_destinations.md) |
| `client.live_event_end` | 3 | [map/operations/live_event_end.md](map/operations/live_event_end.md) |
| `client.live_event_low_latency` | 3 | [map/operations/live_event_low_latency.md](map/operations/live_event_low_latency.md) |
| `client.live_event_sessions` | 2 | [map/operations/live_event_sessions.md](map/operations/live_event_sessions.md) |
| `client.live_event_thumbnails` | 15 | [map/operations/live_event_thumbnails.md](map/operations/live_event_thumbnails.md) |
| `client.live_event_videos` | 12 | [map/operations/live_event_videos.md](map/operations/live_event_videos.md) |
| `client.live_graphics` | 3 | [map/operations/live_graphics.md](map/operations/live_graphics.md) |
| `client.live_scenes` | 5 | [map/operations/live_scenes.md](map/operations/live_scenes.md) |
| `client.on_demand_backgrounds` | 5 | [map/operations/on_demand_backgrounds.md](map/operations/on_demand_backgrounds.md) |
| `client.on_demand_essentials` | 7 | [map/operations/on_demand_essentials.md](map/operations/on_demand_essentials.md) |
| `client.on_demand_genres` | 8 | [map/operations/on_demand_genres.md](map/operations/on_demand_genres.md) |
| `client.on_demand_posters` | 4 | [map/operations/on_demand_posters.md](map/operations/on_demand_posters.md) |
| `client.on_demand_promotions` | 5 | [map/operations/on_demand_promotions.md](map/operations/on_demand_promotions.md) |
| `client.on_demand_purchases_and_rentals` | 3 | [map/operations/on_demand_purchases_and_rentals.md](map/operations/on_demand_purchases_and_rentals.md) |
| `client.on_demand_regions` | 8 | [map/operations/on_demand_regions.md](map/operations/on_demand_regions.md) |
| `client.on_demand_seasons` | 3 | [map/operations/on_demand_seasons.md](map/operations/on_demand_seasons.md) |
| `client.on_demand_videos` | 4 | [map/operations/on_demand_videos.md](map/operations/on_demand_videos.md) |
| `client.payments_essentials` | 4 | [map/operations/payments_essentials.md](map/operations/payments_essentials.md) |
| `client.portfolios_essentials` | 4 | [map/operations/portfolios_essentials.md](map/operations/portfolios_essentials.md) |
| `client.portfolios_videos` | 8 | [map/operations/portfolios_videos.md](map/operations/portfolios_videos.md) |
| `client.search_federated` | 2 | [map/operations/search_federated.md](map/operations/search_federated.md) |
| `client.showcases_custom_showcase_logos` | 5 | [map/operations/showcases_custom_showcase_logos.md](map/operations/showcases_custom_showcase_logos.md) |
| `client.showcases_custom_showcase_thumbnails` | 5 | [map/operations/showcases_custom_showcase_thumbnails.md](map/operations/showcases_custom_showcase_thumbnails.md) |
| `client.showcases_essentials` | 14 | [map/operations/showcases_essentials.md](map/operations/showcases_essentials.md) |
| `client.showcases_showcase_videos` | 16 | [map/operations/showcases_showcase_videos.md](map/operations/showcases_showcase_videos.md) |
| `client.subscription_plans_essentials` | 1 | [map/operations/subscription_plans_essentials.md](map/operations/subscription_plans_essentials.md) |
| `client.tags_essentials` | 1 | [map/operations/tags_essentials.md](map/operations/tags_essentials.md) |
| `client.teams_essentials` | 5 | [map/operations/teams_essentials.md](map/operations/teams_essentials.md) |
| `client.teams_members` | 3 | [map/operations/teams_members.md](map/operations/teams_members.md) |
| `client.tutorial_essentials` | 1 | [map/operations/tutorial_essentials.md](map/operations/tutorial_essentials.md) |
| `client.users_analytics` | 2 | [map/operations/users_analytics.md](map/operations/users_analytics.md) |
| `client.users_essentials` | 4 | [map/operations/users_essentials.md](map/operations/users_essentials.md) |
| `client.users_feeds` | 2 | [map/operations/users_feeds.md](map/operations/users_feeds.md) |
| `client.users_followers` | 12 | [map/operations/users_followers.md](map/operations/users_followers.md) |
| `client.users_lms` | 1 | [map/operations/users_lms.md](map/operations/users_lms.md) |
| `client.users_pictures` | 10 | [map/operations/users_pictures.md](map/operations/users_pictures.md) |
| `client.users_search` | 1 | [map/operations/users_search.md](map/operations/users_search.md) |
| `client.users_watch_history` | 3 | [map/operations/users_watch_history.md](map/operations/users_watch_history.md) |
| `client.videos_ai` | 11 | [map/operations/videos_ai.md](map/operations/videos_ai.md) |
| `client.videos_animated_thumbnails` | 5 | [map/operations/videos_animated_thumbnails.md](map/operations/videos_animated_thumbnails.md) |
| `client.videos_chapters` | 12 | [map/operations/videos_chapters.md](map/operations/videos_chapters.md) |
| `client.videos_content_ratings` | 1 | [map/operations/videos_content_ratings.md](map/operations/videos_content_ratings.md) |
| `client.videos_creative_commons` | 1 | [map/operations/videos_creative_commons.md](map/operations/videos_creative_commons.md) |
| `client.videos_credits` | 8 | [map/operations/videos_credits.md](map/operations/videos_credits.md) |
| `client.videos_embed_privacy` | 3 | [map/operations/videos_embed_privacy.md](map/operations/videos_embed_privacy.md) |
| `client.videos_essentials` | 15 | [map/operations/videos_essentials.md](map/operations/videos_essentials.md) |
| `client.videos_fragments` | 3 | [map/operations/videos_fragments.md](map/operations/videos_fragments.md) |
| `client.videos_languages` | 1 | [map/operations/videos_languages.md](map/operations/videos_languages.md) |
| `client.videos_live_m3_u8_playback` | 2 | [map/operations/videos_live_m3_u8_playback.md](map/operations/videos_live_m3_u8_playback.md) |
| `client.videos_moderation` | 1 | [map/operations/videos_moderation.md](map/operations/videos_moderation.md) |
| `client.videos_nondestructive_trimming` | 1 | [map/operations/videos_nondestructive_trimming.md](map/operations/videos_nondestructive_trimming.md) |
| `client.videos_recommendations` | 1 | [map/operations/videos_recommendations.md](map/operations/videos_recommendations.md) |
| `client.videos_showcases` | 2 | [map/operations/videos_showcases.md](map/operations/videos_showcases.md) |
| `client.videos_tags` | 6 | [map/operations/videos_tags.md](map/operations/videos_tags.md) |
| `client.videos_text_tracks` | 9 | [map/operations/videos_text_tracks.md](map/operations/videos_text_tracks.md) |
| `client.videos_thumbnails` | 7 | [map/operations/videos_thumbnails.md](map/operations/videos_thumbnails.md) |
| `client.videos_transcripts` | 2 | [map/operations/videos_transcripts.md](map/operations/videos_transcripts.md) |
| `client.videos_unlisted_videos` | 6 | [map/operations/videos_unlisted_videos.md](map/operations/videos_unlisted_videos.md) |
| `client.videos_uploads` | 4 | [map/operations/videos_uploads.md](map/operations/videos_uploads.md) |
| `client.videos_versions` | 13 | [map/operations/videos_versions.md](map/operations/videos_versions.md) |
| `client.videos_video_comments` | 9 | [map/operations/videos_video_comments.md](map/operations/videos_video_comments.md) |
| `client.watch_later_queue_essentials` | 8 | [map/operations/watch_later_queue_essentials.md](map/operations/watch_later_queue_essentials.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `vimeo/models/` declares one type plus its input companion, and every module under `vimeo/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`ApiApp` ↔ `api_app.py`; an error alias drops its `Body` suffix: `ActivateLiveEventErrorBody` ↔ `activate_live_event_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 784 | `vimeo/models/` |
| Enums (`Enum` over `str` / `int`) — Python member names + wire values | 281 | `vimeo/models/enums/` |
| Unions (plain) — `TypeAlias` over the arms | 1 | `vimeo/models/unions/` |
| Error aliases (one per Case A operation) | 411 | `vimeo/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`type_` ↔ `"type"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model, enum and union also has an **input companion**, exported beside it from the same package (`ApiApp` ↔ `ApiAppDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str` / `int`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AcceptedCurrencies` ↔ `AcceptedCurrenciesOrStr`) and additionally accepts a wire value this SDK version does not know. A union is a `TypeAlias` over its arms.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `vimeo` |
| Operation controllers | `vimeo.apis` |
| Models | `vimeo.models` |
| Enums | `vimeo.models.enums` |
| Unions | `vimeo.models.unions`, `vimeo.models` |
| Error aliases | `vimeo.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `vimeo.core` |

---

## Servers & auth

**Bearer token.** Pass `bearer="<token>"`.

**OAuth2 (authorization code).** Pass `oauth2_authorization_code` your client id, redirect URI and authorization code; authorization is at `/oauth/authorize` and tokens come from `/oauth/access_token`, both on the base URL — so `base_url="https://…"` moves token traffic too. Scopes are the `Oauth2AuthorizationCodeScope` alias.

**OAuth2 (client credentials).** Pass `oauth2_client_credentials` your client id and secret; tokens come from `/oauth/authorize/client` on the base URL — so `base_url="https://…"` moves token traffic too. Scopes are the `Oauth2ClientCredentialsScope` alias.

**One environment, one server** (`vimeo/server/server_config.py`). The spec declares a single environment, so no `environment` keyword exists; the base URL and its override point:

| Base URL | Override point |
| --- | --- |
| `https://api.vimeo.com` | `base_url="https://…"` |

