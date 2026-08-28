<!-- Generated file — do not edit; regenerated with the SDK. -->

# LikesEssentials — operations

Accessor: `client.likes_essentials` · Source: `vimeo/apis/likes_essentials.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.likes_essentials.check_if_user_liked_video

- **Route**: `GET /users/{user_id}/likes/{video_id}`
- **Signature**: `def check_if_user_liked_video(user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CheckIfUserLikedVideoErrorBody]`
- **Error**: `CheckIfUserLikedVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckIfUserLikedVideoErrorBody` | `vimeo/errors/check_if_user_liked_video_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.likes_essentials.check_if_user_liked_video_alt1

- **Route**: `GET /me/likes/{video_id}`
- **Signature**: `def check_if_user_liked_video_alt1(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CheckIfUserLikedVideoAlt1ErrorBody]`
- **Error**: `CheckIfUserLikedVideoAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckIfUserLikedVideoAlt1ErrorBody` | `vimeo/errors/check_if_user_liked_video_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.likes_essentials.get_likes

- **Route**: `GET /users/{user_id}/likes`
- **Signature**: `def get_likes(user_id: float, *, filter: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort15OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `filter` — query · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetLikesErrorBody]`
- **Error**: `GetLikesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Filter3OrStr` | `vimeo/models/enums/filter3.py` |
| `Sort15OrStr` | `vimeo/models/enums/sort15.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |
| `GetLikesErrorBody` | `vimeo/errors/get_likes_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.likes_essentials.get_likes_alt1

- **Route**: `GET /me/likes`
- **Signature**: `def get_likes_alt1(*, filter: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort15OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `filter` — query · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetLikesAlt1ErrorBody]`
- **Error**: `GetLikesAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Filter3OrStr` | `vimeo/models/enums/filter3.py` |
| `Sort15OrStr` | `vimeo/models/enums/sort15.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |
| `GetLikesAlt1ErrorBody` | `vimeo/errors/get_likes_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.likes_essentials.get_video_likes

- **Route**: `GET /videos/{video_id}/likes`
- **Signature**: `def get_video_likes(video_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `direction` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo/models/enums/sort8.py` |
| `UserConnection` | `vimeo/models/user_connection.py` |

### client.likes_essentials.get_video_likes_alt1

- **Route**: `GET /channels/{channel_id}/videos/{video_id}/likes`
- **Signature**: `def get_video_likes_alt1(channel_id: float, video_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path · `direction` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo/models/enums/sort8.py` |
| `UserConnection` | `vimeo/models/user_connection.py` |

### client.likes_essentials.get_vod_likes

- **Route**: `GET /ondemand/pages/{ondemand_id}/likes`
- **Signature**: `def get_vod_likes(ondemand_id: float, *, direction: DirectionOrStr | None = None, filter: Filter25OrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path · `direction` — query · `filter` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, GetVodLikesErrorBody]`
- **Error**: `GetVodLikesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter25OrStr` | `vimeo/models/enums/filter25.py` |
| `Sort8OrStr` | `vimeo/models/enums/sort8.py` |
| `UserConnection` | `vimeo/models/user_connection.py` |
| `GetVodLikesErrorBody` | `vimeo/errors/get_vod_likes_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.likes_essentials.like_video

- **Route**: `PUT /users/{user_id}/likes/{video_id}`
- **Signature**: `def like_video(user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, LikeVideoErrorBody]`
- **Error**: `LikeVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LikeVideoErrorBody` | `vimeo/errors/like_video_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.likes_essentials.like_video_alt1

- **Route**: `PUT /me/likes/{video_id}`
- **Signature**: `def like_video_alt1(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, LikeVideoAlt1ErrorBody]`
- **Error**: `LikeVideoAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LikeVideoAlt1ErrorBody` | `vimeo/errors/like_video_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.likes_essentials.unlike_video

- **Route**: `DELETE /users/{user_id}/likes/{video_id}`
- **Signature**: `def unlike_video(user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UnlikeVideoErrorBody]`
- **Error**: `UnlikeVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UnlikeVideoErrorBody` | `vimeo/errors/unlike_video_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.likes_essentials.unlike_video_alt1

- **Route**: `DELETE /me/likes/{video_id}`
- **Signature**: `def unlike_video_alt1(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UnlikeVideoAlt1ErrorBody]`
- **Error**: `UnlikeVideoAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UnlikeVideoAlt1ErrorBody` | `vimeo/errors/unlike_video_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

