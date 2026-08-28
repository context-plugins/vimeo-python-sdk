<!-- Generated file — do not edit; regenerated with the SDK. -->

# GroupsVideos — operations

Accessor: `client.groups_videos` · Source: `vimeo/apis/groups_videos.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.groups_videos.add_video_to_group

- **Route**: `PUT /groups/{group_id}/videos/{video_id}`
- **Signature**: `def add_video_to_group(group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`, `video_id`
- **Params**: `group_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, AddVideoToGroupErrorBody]`
- **Error**: `AddVideoToGroupErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo/models/video.py` |
| `AddVideoToGroupErrorBody` | `vimeo/errors/add_video_to_group_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.groups_videos.delete_video_from_group

- **Route**: `DELETE /groups/{group_id}/videos/{video_id}`
- **Signature**: `def delete_video_from_group(group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`, `video_id`
- **Params**: `group_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoFromGroupErrorBody]`
- **Error**: `DeleteVideoFromGroupErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoFromGroupErrorBody` | `vimeo/errors/delete_video_from_group_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.groups_videos.get_available_video_groups

- **Route**: `GET /videos/{video_id}/available_groups`
- **Signature**: `def get_available_video_groups(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `GroupConnection`
- **Returns (raw)**: `ApiResult[GroupConnection, GetAvailableVideoGroupsErrorBody]`
- **Error**: `GetAvailableVideoGroupsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GroupConnection` | `vimeo/models/group_connection.py` |
| `GetAvailableVideoGroupsErrorBody` | `vimeo/errors/get_available_video_groups_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.groups_videos.get_group_video

- **Route**: `GET /groups/{group_id}/videos/{video_id}`
- **Signature**: `def get_group_video(group_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`, `video_id`
- **Params**: `group_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, GetGroupVideoErrorBody]`
- **Error**: `GetGroupVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo/models/video.py` |
| `GetGroupVideoErrorBody` | `vimeo/errors/get_group_video_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.groups_videos.get_group_videos

- **Route**: `GET /groups/{group_id}/videos`
- **Signature**: `def get_group_videos(group_id: float, *, direction: DirectionOrStr | None = None, filter: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort15OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`
- **Params**: `group_id` — path · `direction` — query · `filter` — query · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetGroupVideosErrorBody]`
- **Error**: `GetGroupVideosErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter3OrStr` | `vimeo/models/enums/filter3.py` |
| `Sort15OrStr` | `vimeo/models/enums/sort15.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |
| `GetGroupVideosErrorBody` | `vimeo/errors/get_group_videos_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

