<!-- Generated file — do not edit; regenerated with the SDK. -->

# ChannelsVideos — operations

Accessor: `client.channels_videos` · Source: `vimeo/apis/channels_videos.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.channels_videos.add_video_to_channel

- **Route**: `PUT /channels/{channel_id}/videos/{video_id}`
- **Signature**: `def add_video_to_channel(channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideoToChannelErrorBody]`
- **Error**: `AddVideoToChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddVideoToChannelErrorBody` | `vimeo/errors/add_video_to_channel_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_videos.add_videos_to_channel

- **Route**: `PUT /channels/{channel_id}/videos`
- **Signature**: `def add_videos_to_channel(channel_id: float, body: ChannelsVideosRequest1 | ChannelsVideosRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `body`
- **Params**: `channel_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideosToChannelErrorBody]`
- **Error**: `AddVideosToChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsVideosRequest1` | `vimeo/models/channels_videos_request1.py` |
| `ChannelsVideosRequest1Dict` | `vimeo/models/channels_videos_request1.py` |
| `AddVideosToChannelErrorBody` | `vimeo/errors/add_videos_to_channel_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_videos.delete_video_from_channel

- **Route**: `DELETE /channels/{channel_id}/videos/{video_id}`
- **Signature**: `def delete_video_from_channel(channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoFromChannelErrorBody]`
- **Error**: `DeleteVideoFromChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoFromChannelErrorBody` | `vimeo/errors/delete_video_from_channel_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_videos.get_available_video_channels

- **Route**: `GET /videos/{video_id}/available_channels`
- **Signature**: `def get_available_video_channels(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `ChannelConnection`
- **Returns (raw)**: `ApiResult[ChannelConnection, GetAvailableVideoChannelsErrorBody]`
- **Error**: `GetAvailableVideoChannelsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelConnection` | `vimeo/models/channel_connection.py` |
| `GetAvailableVideoChannelsErrorBody` | `vimeo/errors/get_available_video_channels_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_videos.get_channel_video

- **Route**: `GET /channels/{channel_id}/videos/{video_id}`
- **Signature**: `def get_channel_video(channel_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, GetChannelVideoErrorBody]`
- **Error**: `GetChannelVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo/models/video.py` |
| `GetChannelVideoErrorBody` | `vimeo/errors/get_channel_video_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_videos.get_channel_videos

- **Route**: `GET /channels/{channel_id}/videos`
- **Signature**: `def get_channel_videos(channel_id: float, *, containing_uri: str | None = None, direction: DirectionOrStr | None = None, filter: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sizes: str | None = None, sort: Sort10OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path · `containing_uri` — query · `direction` — query · `filter` — query · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sizes` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetChannelVideosErrorBody]`
- **Error**: `GetChannelVideosErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter3OrStr` | `vimeo/models/enums/filter3.py` |
| `Sort10OrStr` | `vimeo/models/enums/sort10.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |
| `GetChannelVideosErrorBody` | `vimeo/errors/get_channel_videos_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_videos.remove_videos_from_channel

- **Route**: `DELETE /channels/{channel_id}/videos`
- **Signature**: `def remove_videos_from_channel(channel_id: float, body: ChannelsVideosRequest | ChannelsVideosRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `body`
- **Params**: `channel_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveVideosFromChannelErrorBody]`
- **Error**: `RemoveVideosFromChannelErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsVideosRequest` | `vimeo/models/channels_videos_request.py` |
| `ChannelsVideosRequestDict` | `vimeo/models/channels_videos_request.py` |
| `RemoveVideosFromChannelErrorBody` | `vimeo/errors/remove_videos_from_channel_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

