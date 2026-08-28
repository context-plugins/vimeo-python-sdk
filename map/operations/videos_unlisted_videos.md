<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosUnlistedVideos — operations

Accessor: `client.videos_unlisted_videos` · Source: `vimeo/apis/videos_unlisted_videos.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_unlisted_videos.add_video_privacy_user

- **Route**: `PUT /videos/{video_id}/privacy/users/{user_id}`
- **Signature**: `def add_video_privacy_user(user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, AddVideoPrivacyUserErrorBody]`
- **Error**: `AddVideoPrivacyUserErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `User` | `vimeo/models/user.py` |
| `AddVideoPrivacyUserErrorBody` | `vimeo/errors/add_video_privacy_user_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_unlisted_videos.add_video_privacy_users

- **Route**: `PUT /videos/{video_id}/privacy/users`
- **Signature**: `def add_video_privacy_users(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `list[User]`
- **Returns (raw)**: `ApiResult[list[User], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `User` | `vimeo/models/user.py` |

### client.videos_unlisted_videos.add_video_privacy_users_alt1

- **Route**: `PUT /channels/{channel_id}/videos/{video_id}/privacy/users`
- **Signature**: `def add_video_privacy_users_alt1(channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path
- **Returns (parsed)**: `list[User]`
- **Returns (raw)**: `ApiResult[list[User], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `User` | `vimeo/models/user.py` |

### client.videos_unlisted_videos.delete_video_privacy_user

- **Route**: `DELETE /videos/{video_id}/privacy/users/{user_id}`
- **Signature**: `def delete_video_privacy_user(user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoPrivacyUserErrorBody]`
- **Error**: `DeleteVideoPrivacyUserErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoPrivacyUserErrorBody` | `vimeo/errors/delete_video_privacy_user_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_unlisted_videos.get_video_privacy_users

- **Route**: `GET /videos/{video_id}/privacy/users`
- **Signature**: `def get_video_privacy_users(video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, GetVideoPrivacyUsersErrorBody]`
- **Error**: `GetVideoPrivacyUsersErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UserConnection` | `vimeo/models/user_connection.py` |
| `GetVideoPrivacyUsersErrorBody` | `vimeo/errors/get_video_privacy_users_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_unlisted_videos.get_video_privacy_users_alt1

- **Route**: `GET /channels/{channel_id}/videos/{video_id}/privacy/users`
- **Signature**: `def get_video_privacy_users_alt1(channel_id: float, video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, GetVideoPrivacyUsersAlt1ErrorBody]`
- **Error**: `GetVideoPrivacyUsersAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UserConnection` | `vimeo/models/user_connection.py` |
| `GetVideoPrivacyUsersAlt1ErrorBody` | `vimeo/errors/get_video_privacy_users_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

