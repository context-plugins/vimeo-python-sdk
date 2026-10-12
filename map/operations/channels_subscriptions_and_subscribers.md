<!-- Generated file — do not edit; regenerated with the SDK. -->

# ChannelsSubscriptionsAndSubscribers — operations

Accessor: `client.channels_subscriptions_and_subscribers` · Source: `vimeo_api/apis/channels_subscriptions_and_subscribers.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.channels_subscriptions_and_subscribers.check_if_user_subscribed_to_channel

- **Route**: `GET /users/{user_id}/channels/{channel_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_if_user_subscribed_to_channel(channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `user_id`
- **Params**: `channel_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CheckIfUserSubscribedToChannelErrorBody]`
- **Error**: `CheckIfUserSubscribedToChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckIfUserSubscribedToChannelErrorBody` | `vimeo_api/errors/check_if_user_subscribed_to_channel_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.channels_subscriptions_and_subscribers.check_if_user_subscribed_to_channel_alt1

- **Route**: `GET /me/channels/{channel_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_if_user_subscribed_to_channel_alt1(channel_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CheckIfUserSubscribedToChannelAlt1ErrorBody]`
- **Error**: `CheckIfUserSubscribedToChannelAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckIfUserSubscribedToChannelAlt1ErrorBody` | `vimeo_api/errors/check_if_user_subscribed_to_channel_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.channels_subscriptions_and_subscribers.get_channel_subscribers

- **Route**: `GET /channels/{channel_id}/users`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_channel_subscribers(channel_id: float, filter_: Filter2OrStr, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `filter_`
- **Params**: `channel_id` — path · `filter_` — query `filter` · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, GetChannelSubscribersErrorBody]`
- **Error**: `GetChannelSubscribersErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Filter2OrStr` | `vimeo_api/models/enums/filter2.py` |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `UserConnection` | `vimeo_api/models/user_connection.py` |
| `GetChannelSubscribersErrorBody` | `vimeo_api/errors/get_channel_subscribers_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.channels_subscriptions_and_subscribers.subscribe_to_channel

- **Route**: `PUT /users/{user_id}/channels/{channel_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def subscribe_to_channel(channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `user_id`
- **Params**: `channel_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SubscribeToChannelErrorBody]`
- **Error**: `SubscribeToChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubscribeToChannelErrorBody` | `vimeo_api/errors/subscribe_to_channel_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.channels_subscriptions_and_subscribers.subscribe_to_channel_alt1

- **Route**: `PUT /me/channels/{channel_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def subscribe_to_channel_alt1(channel_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SubscribeToChannelAlt1ErrorBody]`
- **Error**: `SubscribeToChannelAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubscribeToChannelAlt1ErrorBody` | `vimeo_api/errors/subscribe_to_channel_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.channels_subscriptions_and_subscribers.unsubscribe_from_channel

- **Route**: `DELETE /users/{user_id}/channels/{channel_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def unsubscribe_from_channel(channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `user_id`
- **Params**: `channel_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UnsubscribeFromChannelErrorBody]`
- **Error**: `UnsubscribeFromChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UnsubscribeFromChannelErrorBody` | `vimeo_api/errors/unsubscribe_from_channel_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.channels_subscriptions_and_subscribers.unsubscribe_from_channel_alt1

- **Route**: `DELETE /me/channels/{channel_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def unsubscribe_from_channel_alt1(channel_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UnsubscribeFromChannelAlt1ErrorBody]`
- **Error**: `UnsubscribeFromChannelAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UnsubscribeFromChannelAlt1ErrorBody` | `vimeo_api/errors/unsubscribe_from_channel_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

