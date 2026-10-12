<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnDemandVideos — operations

Accessor: `client.on_demand_videos` · Source: `vimeo_api/apis/on_demand_videos.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_demand_videos.add_video_to_vod

- **Route**: `PUT /ondemand/pages/{ondemand_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_video_to_vod(ondemand_id: float, video_id: float, body: OndemandPagesVideosRequest | OndemandPagesVideosRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `video_id`, `body`
- **Params**: `ondemand_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `OnDemandVideo`
- **Returns (raw)**: `ApiResult[OnDemandVideo, AddVideoToVodErrorBody]`
- **Error**: `AddVideoToVodErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OndemandPagesVideosRequest` | `vimeo_api/models/ondemand_pages_videos_request.py` |
| `OndemandPagesVideosRequestDict` | `vimeo_api/models/ondemand_pages_videos_request.py` |
| `OnDemandVideo` | `vimeo_api/models/on_demand_video.py` |
| `AddVideoToVodErrorBody` | `vimeo_api/errors/add_video_to_vod_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_videos.delete_video_from_vod

- **Route**: `DELETE /ondemand/pages/{ondemand_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_video_from_vod(ondemand_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `video_id`
- **Params**: `ondemand_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoFromVodErrorBody]`
- **Error**: `DeleteVideoFromVodErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoFromVodErrorBody` | `vimeo_api/errors/delete_video_from_vod_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_videos.get_vod_video

- **Route**: `GET /ondemand/pages/{ondemand_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_video(ondemand_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `video_id`
- **Params**: `ondemand_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |

### client.on_demand_videos.get_vod_videos

- **Route**: `GET /ondemand/pages/{ondemand_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_videos(ondemand_id: float, *, direction: DirectionOrStr | None = None, filter_: Filter29OrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort45OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path · `direction` — query · `filter_` — query `filter` · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `OnDemandVideoConnection`
- **Returns (raw)**: `ApiResult[OnDemandVideoConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter29OrStr` | `vimeo_api/models/enums/filter29.py` |
| `Sort45OrStr` | `vimeo_api/models/enums/sort45.py` |
| `OnDemandVideoConnection` | `vimeo_api/models/on_demand_video_connection.py` |

