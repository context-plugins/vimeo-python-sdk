<!-- Generated file — do not edit; regenerated with the SDK. -->

# WatchLaterQueueEssentials — operations

Accessor: `client.watch_later_queue_essentials` · Source: `vimeo/apis/watch_later_queue_essentials.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.watch_later_queue_essentials.add_video_to_watch_later

- **Route**: `PUT /users/{user_id}/watchlater/{video_id}`
- **Signature**: `def add_video_to_watch_later(user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.watch_later_queue_essentials.add_video_to_watch_later_alt1

- **Route**: `PUT /me/watchlater/{video_id}`
- **Signature**: `def add_video_to_watch_later_alt1(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.watch_later_queue_essentials.check_watch_later_queue

- **Route**: `GET /users/{user_id}/watchlater/{video_id}`
- **Signature**: `def check_watch_later_queue(user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, CheckWatchLaterQueueErrorBody]`
- **Error**: `CheckWatchLaterQueueErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo/models/video.py` |
| `CheckWatchLaterQueueErrorBody` | `vimeo/errors/check_watch_later_queue_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.watch_later_queue_essentials.check_watch_later_queue_alt1

- **Route**: `GET /me/watchlater/{video_id}`
- **Signature**: `def check_watch_later_queue_alt1(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, CheckWatchLaterQueueAlt1ErrorBody]`
- **Error**: `CheckWatchLaterQueueAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo/models/video.py` |
| `CheckWatchLaterQueueAlt1ErrorBody` | `vimeo/errors/check_watch_later_queue_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.watch_later_queue_essentials.delete_video_from_watch_later

- **Route**: `DELETE /users/{user_id}/watchlater/{video_id}`
- **Signature**: `def delete_video_from_watch_later(user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.watch_later_queue_essentials.delete_video_from_watch_later_alt1

- **Route**: `DELETE /me/watchlater/{video_id}`
- **Signature**: `def delete_video_from_watch_later_alt1(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.watch_later_queue_essentials.get_watch_later_queue

- **Route**: `GET /users/{user_id}/watchlater`
- **Signature**: `def get_watch_later_queue(user_id: float, *, direction: DirectionOrStr | None = None, filter: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort15OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `filter` — query · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter3OrStr` | `vimeo/models/enums/filter3.py` |
| `Sort15OrStr` | `vimeo/models/enums/sort15.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |

### client.watch_later_queue_essentials.get_watch_later_queue_alt1

- **Route**: `GET /me/watchlater`
- **Signature**: `def get_watch_later_queue_alt1(*, direction: DirectionOrStr | None = None, filter: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort15OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter` — query · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter3OrStr` | `vimeo/models/enums/filter3.py` |
| `Sort15OrStr` | `vimeo/models/enums/sort15.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |

