<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosNondestructiveTrimming — operations

Accessor: `client.videos_nondestructive_trimming` · Source: `vimeo/apis/videos_nondestructive_trimming.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_nondestructive_trimming.clip_trim

- **Route**: `POST /videos/{video_id}/trim`
- **Signature**: `def clip_trim(video_id: float, *, body: VideosTrimRequest | VideosTrimRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `TrimmedVideo`
- **Returns (raw)**: `ApiResult[TrimmedVideo, ClipTrimErrorBody]`
- **Error**: `ClipTrimErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosTrimRequest` | `vimeo/models/videos_trim_request.py` |
| `VideosTrimRequestDict` | `vimeo/models/videos_trim_request.py` |
| `TrimmedVideo` | `vimeo/models/trimmed_video.py` |
| `ClipTrimErrorBody` | `vimeo/errors/clip_trim_error.py` |
| `Error` | `vimeo/models/error.py` |

