<!-- Generated file — do not edit; regenerated with the SDK. -->

# ChannelsModerators — operations

Accessor: `client.channels_moderators` · Source: `vimeo_api/apis/channels_moderators.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.channels_moderators.add_channel_moderator

- **Route**: `PUT /channels/{channel_id}/moderators/{user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_channel_moderator(channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `user_id`
- **Params**: `channel_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddChannelModeratorErrorBody]`
- **Error**: `AddChannelModeratorErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddChannelModeratorErrorBody` | `vimeo_api/errors/add_channel_moderator_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.channels_moderators.add_channel_moderators

- **Route**: `PUT /channels/{channel_id}/moderators`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_channel_moderators(channel_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddChannelModeratorsErrorBody]`
- **Error**: `AddChannelModeratorsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddChannelModeratorsErrorBody` | `vimeo_api/errors/add_channel_moderators_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.channels_moderators.get_channel_moderator

- **Route**: `GET /channels/{channel_id}/moderators/{user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_channel_moderator(channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `user_id`
- **Params**: `channel_id` — path · `user_id` — path
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `User` | `vimeo_api/models/user.py` |

### client.channels_moderators.get_channel_moderators

- **Route**: `GET /channels/{channel_id}/moderators`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_channel_moderators(channel_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `UserConnection` | `vimeo_api/models/user_connection.py` |

### client.channels_moderators.remove_channel_moderator

- **Route**: `DELETE /channels/{channel_id}/moderators/{user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def remove_channel_moderator(channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `user_id`
- **Params**: `channel_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveChannelModeratorErrorBody]`
- **Error**: `RemoveChannelModeratorErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveChannelModeratorErrorBody` | `vimeo_api/errors/remove_channel_moderator_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.channels_moderators.remove_channel_moderators

- **Route**: `DELETE /channels/{channel_id}/moderators`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def remove_channel_moderators(channel_id: float, body: ChannelsModeratorsRequest | ChannelsModeratorsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `body`
- **Params**: `channel_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveChannelModeratorsErrorBody]`
- **Error**: `RemoveChannelModeratorsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsModeratorsRequest` | `vimeo_api/models/channels_moderators_request.py` |
| `ChannelsModeratorsRequestDict` | `vimeo_api/models/channels_moderators_request.py` |
| `RemoveChannelModeratorsErrorBody` | `vimeo_api/errors/remove_channel_moderators_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.channels_moderators.replace_channel_moderators

- **Route**: `PATCH /channels/{channel_id}/moderators`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def replace_channel_moderators(channel_id: float, body: ChannelsModeratorsRequest1 | ChannelsModeratorsRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `body`
- **Params**: `channel_id` — path · `body` — JSON body
- **Returns (parsed)**: `list[User]`
- **Returns (raw)**: `ApiResult[list[User], ReplaceChannelModeratorsErrorBody]`
- **Error**: `ReplaceChannelModeratorsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsModeratorsRequest1` | `vimeo_api/models/channels_moderators_request1.py` |
| `ChannelsModeratorsRequest1Dict` | `vimeo_api/models/channels_moderators_request1.py` |
| `User` | `vimeo_api/models/user.py` |
| `ReplaceChannelModeratorsErrorBody` | `vimeo_api/errors/replace_channel_moderators_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

