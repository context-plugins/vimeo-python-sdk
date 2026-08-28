<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosUploads — operations

Accessor: `client.videos_uploads` · Source: `vimeo/apis/videos_uploads.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_uploads.complete_streaming_upload

- **Route**: `DELETE /users/{user_id}/uploads/{upload_id}`
- **Signature**: `def complete_streaming_upload(upload_id: float, user_id: float, signature: str, video_file_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `upload_id`, `user_id`, `signature`, `video_file_id`
- **Params**: `upload_id` — path · `user_id` — path · `signature` — query · `video_file_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CompleteStreamingUploadErrorBody]`
- **Error**: `CompleteStreamingUploadErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CompleteStreamingUploadErrorBody` | `vimeo/errors/complete_streaming_upload_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_uploads.get_upload_attempt

- **Route**: `GET /users/{user_id}/uploads/{upload_id}`
- **Signature**: `def get_upload_attempt(upload_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `upload_id`, `user_id`
- **Params**: `upload_id` — path · `user_id` — path
- **Returns (parsed)**: `UploadAttempt`
- **Returns (raw)**: `ApiResult[UploadAttempt, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UploadAttempt` | `vimeo/models/upload_attempt.py` |

### client.videos_uploads.upload_video

- **Route**: `POST /users/{user_id}/videos`
- **Signature**: `def upload_video(user_id: float, body: UsersVideosRequest1 | UsersVideosRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `body`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, UploadVideoErrorBody]`
- **Error**: `UploadVideoErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersVideosRequest1` | `vimeo/models/users_videos_request1.py` |
| `UsersVideosRequest1Dict` | `vimeo/models/users_videos_request1.py` |
| `Video` | `vimeo/models/video.py` |
| `UploadVideoErrorBody` | `vimeo/errors/upload_video_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_uploads.upload_video_alt1

- **Route**: `POST /me/videos`
- **Signature**: `def upload_video_alt1(body: MeVideosRequest1 | MeVideosRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, UploadVideoAlt1ErrorBody]`
- **Error**: `UploadVideoAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeVideosRequest1` | `vimeo/models/me_videos_request1.py` |
| `MeVideosRequest1Dict` | `vimeo/models/me_videos_request1.py` |
| `Video` | `vimeo/models/video.py` |
| `UploadVideoAlt1ErrorBody` | `vimeo/errors/upload_video_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

