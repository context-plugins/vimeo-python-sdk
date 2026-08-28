<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersWatchHistory — operations

Accessor: `client.users_watch_history` · Source: `vimeo/apis/users_watch_history.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.users_watch_history.delete_from_watch_history

- **Route**: `DELETE /me/watched/videos/{video_id}`
- **Signature**: `def delete_from_watch_history(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.users_watch_history.delete_watch_history

- **Route**: `DELETE /me/watched/videos`
- **Signature**: `def delete_watch_history(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.users_watch_history.get_watch_history

- **Route**: `GET /me/watched/videos`
- **Signature**: `def get_watch_history(*, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetWatchHistoryErrorBody]`
- **Error**: `GetWatchHistoryErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideoConnection` | `vimeo/models/video_connection.py` |
| `GetWatchHistoryErrorBody` | `vimeo/errors/get_watch_history_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

