<!-- Generated file — do not edit; regenerated with the SDK. -->

# ChannelsPrivateChannelMembers — operations

Accessor: `client.channels_private_channel_members` · Source: `vimeo/apis/channels_private_channel_members.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.channels_private_channel_members.delete_channel_privacy_user

- **Route**: `DELETE /channels/{channel_id}/privacy/users/{user_id}`
- **Signature**: `def delete_channel_privacy_user(channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `user_id`
- **Params**: `channel_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteChannelPrivacyUserErrorBody]`
- **Error**: `DeleteChannelPrivacyUserErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteChannelPrivacyUserErrorBody` | `vimeo/errors/delete_channel_privacy_user_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.channels_private_channel_members.get_channel_privacy_users

- **Route**: `GET /channels/{channel_id}/privacy/users`
- **Signature**: `def get_channel_privacy_users(channel_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path · `direction` — query · `page` — query · `per_page` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, GetChannelPrivacyUsersErrorBody]`
- **Error**: `GetChannelPrivacyUsersErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `UserConnection` | `vimeo/models/user_connection.py` |
| `GetChannelPrivacyUsersErrorBody` | `vimeo/errors/get_channel_privacy_users_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.channels_private_channel_members.set_channel_privacy_user

- **Route**: `PUT /channels/{channel_id}/privacy/users/{user_id}`
- **Signature**: `def set_channel_privacy_user(channel_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `user_id`
- **Params**: `channel_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SetChannelPrivacyUserErrorBody]`
- **Error**: `SetChannelPrivacyUserErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetChannelPrivacyUserErrorBody` | `vimeo/errors/set_channel_privacy_user_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.channels_private_channel_members.set_channel_privacy_users

- **Route**: `PUT /channels/{channel_id}/privacy/users`
- **Signature**: `def set_channel_privacy_users(channel_id: float, body: ChannelsPrivacyUsersRequest | ChannelsPrivacyUsersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `body`
- **Params**: `channel_id` — path · `body` — JSON body
- **Returns (parsed)**: `list[User]`
- **Returns (raw)**: `ApiResult[list[User], SetChannelPrivacyUsersErrorBody]`
- **Error**: `SetChannelPrivacyUsersErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsPrivacyUsersRequest` | `vimeo/models/channels_privacy_users_request.py` |
| `ChannelsPrivacyUsersRequestDict` | `vimeo/models/channels_privacy_users_request.py` |
| `User` | `vimeo/models/user.py` |
| `SetChannelPrivacyUsersErrorBody` | `vimeo/errors/set_channel_privacy_users_error.py` |
| `Error` | `vimeo/models/error.py` |

