<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosAnimatedThumbnails — operations

Accessor: `client.videos_animated_thumbnails` · Source: `vimeo/apis/videos_animated_thumbnails.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_animated_thumbnails.create_animated_thumbset

- **Route**: `POST /videos/{video_id}/animated_thumbsets`
- **Signature**: `def create_animated_thumbset(video_id: float, body: VideosAnimatedThumbsetsRequest | VideosAnimatedThumbsetsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `body`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `AnimatedThumbset`
- **Returns (raw)**: `ApiResult[AnimatedThumbset, CreateAnimatedThumbsetErrorBody]`
- **Error**: `CreateAnimatedThumbsetErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `LegacyError` [403, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosAnimatedThumbsetsRequest` | `vimeo/models/videos_animated_thumbsets_request.py` |
| `VideosAnimatedThumbsetsRequestDict` | `vimeo/models/videos_animated_thumbsets_request.py` |
| `AnimatedThumbset` | `vimeo/models/animated_thumbset.py` |
| `CreateAnimatedThumbsetErrorBody` | `vimeo/errors/create_animated_thumbset_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_animated_thumbnails.delete_animated_thumbset

- **Route**: `DELETE /videos/{video_id}/animated_thumbsets/{picture_id}`
- **Signature**: `def delete_animated_thumbset(picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `picture_id`, `video_id`
- **Params**: `picture_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteAnimatedThumbsetErrorBody]`
- **Error**: `DeleteAnimatedThumbsetErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteAnimatedThumbsetErrorBody` | `vimeo/errors/delete_animated_thumbset_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_animated_thumbnails.get_all_animated_thumbset

- **Route**: `GET /videos/{video_id}/animated_thumbsets`
- **Signature**: `def get_all_animated_thumbset(video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `AnimatedThumbsetConnection`
- **Returns (raw)**: `ApiResult[AnimatedThumbsetConnection, GetAllAnimatedThumbsetErrorBody]`
- **Error**: `GetAllAnimatedThumbsetErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AnimatedThumbsetConnection` | `vimeo/models/animated_thumbset_connection.py` |
| `GetAllAnimatedThumbsetErrorBody` | `vimeo/errors/get_all_animated_thumbset_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_animated_thumbnails.get_animated_thumbset

- **Route**: `GET /videos/{video_id}/animated_thumbsets/{picture_id}`
- **Signature**: `def get_animated_thumbset(picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `picture_id`, `video_id`
- **Params**: `picture_id` — path · `video_id` — path
- **Returns (parsed)**: `AnimatedThumbset`
- **Returns (raw)**: `ApiResult[AnimatedThumbset, GetAnimatedThumbsetErrorBody]`
- **Error**: `GetAnimatedThumbsetErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AnimatedThumbset` | `vimeo/models/animated_thumbset.py` |
| `GetAnimatedThumbsetErrorBody` | `vimeo/errors/get_animated_thumbset_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_animated_thumbnails.get_animated_thumbset_status

- **Route**: `GET /videos/{video_id}/animated_thumbsets/{picture_id}/status`
- **Signature**: `def get_animated_thumbset_status(picture_id: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `picture_id`, `video_id`
- **Params**: `picture_id` — path · `video_id` — path
- **Returns (parsed)**: `AnimatedThumbset`
- **Returns (raw)**: `ApiResult[AnimatedThumbset, GetAnimatedThumbsetStatusErrorBody]`
- **Error**: `GetAnimatedThumbsetStatusErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AnimatedThumbset` | `vimeo/models/animated_thumbset.py` |
| `GetAnimatedThumbsetStatusErrorBody` | `vimeo/errors/get_animated_thumbset_status_error.py` |
| `Error` | `vimeo/models/error.py` |

