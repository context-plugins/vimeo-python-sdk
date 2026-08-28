<!-- Generated file — do not edit; regenerated with the SDK. -->

# ChannelsEssentials — operations

Accessor: `client.channels_essentials` · Source: `vimeo/apis/channels_essentials.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.channels_essentials.create_channel

- **Route**: `POST /channels`
- **Signature**: `def create_channel(body: ChannelsRequest | ChannelsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Channel`
- **Returns (raw)**: `ApiResult[Channel, CreateChannelErrorBody]`
- **Error**: `CreateChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsRequest` | `vimeo/models/channels_request.py` |
| `ChannelsRequestDict` | `vimeo/models/channels_request.py` |
| `Channel` | `vimeo/models/channel.py` |
| `CreateChannelErrorBody` | `vimeo/errors/create_channel_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_essentials.delete_channel

- **Route**: `DELETE /channels/{channel_id}`
- **Signature**: `def delete_channel(channel_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteChannelErrorBody]`
- **Error**: `DeleteChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteChannelErrorBody` | `vimeo/errors/delete_channel_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_essentials.edit_channel

- **Route**: `PATCH /channels/{channel_id}`
- **Signature**: `def edit_channel(channel_id: float, *, body: ChannelsRequest1 | ChannelsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path · `body` — JSON body
- **Returns (parsed)**: `Channel`
- **Returns (raw)**: `ApiResult[Channel, EditChannelErrorBody]`
- **Error**: `EditChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsRequest1` | `vimeo/models/channels_request1.py` |
| `ChannelsRequest1Dict` | `vimeo/models/channels_request1.py` |
| `Channel` | `vimeo/models/channel.py` |
| `EditChannelErrorBody` | `vimeo/errors/edit_channel_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_essentials.get_channel

- **Route**: `GET /channels/{channel_id}`
- **Signature**: `def get_channel(channel_id: float, *, sizes: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path · `sizes` — query
- **Returns (parsed)**: `Channel`
- **Returns (raw)**: `ApiResult[Channel, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Channel` | `vimeo/models/channel.py` |

### client.channels_essentials.get_channel_subscriptions

- **Route**: `GET /users/{user_id}/channels`
- **Signature**: `def get_channel_subscriptions(user_id: float, *, direction: DirectionOrStr | None = None, filter: Filter12OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort4OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `filter` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `ChannelConnection`
- **Returns (raw)**: `ApiResult[ChannelConnection, GetChannelSubscriptionsErrorBody]`
- **Error**: `GetChannelSubscriptionsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter12OrStr` | `vimeo/models/enums/filter12.py` |
| `Sort4OrStr` | `vimeo/models/enums/sort4.py` |
| `ChannelConnection` | `vimeo/models/channel_connection.py` |
| `GetChannelSubscriptionsErrorBody` | `vimeo/errors/get_channel_subscriptions_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.channels_essentials.get_channel_subscriptions_alt1

- **Route**: `GET /me/channels`
- **Signature**: `def get_channel_subscriptions_alt1(*, direction: DirectionOrStr | None = None, filter: Filter12OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort4OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `ChannelConnection`
- **Returns (raw)**: `ApiResult[ChannelConnection, GetChannelSubscriptionsAlt1ErrorBody]`
- **Error**: `GetChannelSubscriptionsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter12OrStr` | `vimeo/models/enums/filter12.py` |
| `Sort4OrStr` | `vimeo/models/enums/sort4.py` |
| `ChannelConnection` | `vimeo/models/channel_connection.py` |
| `GetChannelSubscriptionsAlt1ErrorBody` | `vimeo/errors/get_channel_subscriptions_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.channels_essentials.get_channels

- **Route**: `GET /channels`
- **Signature**: `def get_channels(*, direction: DirectionOrStr | None = None, filter: Filter1OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort7OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `ChannelConnection`
- **Returns (raw)**: `ApiResult[ChannelConnection, GetChannelsErrorBody]`
- **Error**: `GetChannelsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter1OrStr` | `vimeo/models/enums/filter1.py` |
| `Sort7OrStr` | `vimeo/models/enums/sort7.py` |
| `ChannelConnection` | `vimeo/models/channel_connection.py` |
| `GetChannelsErrorBody` | `vimeo/errors/get_channels_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |
| `Error` | `vimeo/models/error.py` |

