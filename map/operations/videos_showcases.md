<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosShowcases — operations

Accessor: `client.videos_showcases` · Source: `vimeo_api/apis/videos_showcases.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_showcases.add_or_remove_multiple_albums

- **Route**: `PATCH /videos/{video_id}/albums`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_or_remove_multiple_albums(video_id: float, *, body: VideosAlbumsRequest | VideosAlbumsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `list[Album]`
- **Returns (raw)**: `ApiResult[list[Album], AddOrRemoveMultipleAlbumsErrorBody]`
- **Error**: `AddOrRemoveMultipleAlbumsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosAlbumsRequest` | `vimeo_api/models/videos_albums_request.py` |
| `VideosAlbumsRequestDict` | `vimeo_api/models/videos_albums_request.py` |
| `Album` | `vimeo_api/models/album.py` |
| `AddOrRemoveMultipleAlbumsErrorBody` | `vimeo_api/errors/add_or_remove_multiple_albums_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.videos_showcases.get_video_albums

- **Route**: `GET /videos/{video_id}/albums`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_video_albums(video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `AlbumConnection`
- **Returns (raw)**: `ApiResult[AlbumConnection, GetVideoAlbumsErrorBody]`
- **Error**: `GetVideoAlbumsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AlbumConnection` | `vimeo_api/models/album_connection.py` |
| `GetVideoAlbumsErrorBody` | `vimeo_api/errors/get_video_albums_error.py` |
| `Error` | `vimeo_api/models/error.py` |

