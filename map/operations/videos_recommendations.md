<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosRecommendations — operations

Accessor: `client.videos_recommendations` · Source: `vimeo_api/apis/videos_recommendations.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_recommendations.get_related_videos

- **Route**: `GET /videos/{video_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_related_videos(video_id: float, *, filter_: Filter46OrStr | None = None, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `filter_` — query `filter` · `page` — query · `per_page` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetRelatedVideosErrorBody]`
- **Error**: `GetRelatedVideosErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Filter46OrStr` | `vimeo_api/models/enums/filter46.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `GetRelatedVideosErrorBody` | `vimeo_api/errors/get_related_videos_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |
| `Error` | `vimeo_api/models/error.py` |

