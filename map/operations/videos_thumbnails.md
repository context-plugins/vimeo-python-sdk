<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosThumbnails — operations

Accessor: `client.videos_thumbnails` · Source: `vimeo/apis/videos_thumbnails.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.videos_thumbnails.create_video_thumbnail

- **Route**: `POST /videos/{video_id}/pictures`
- **Signature**: `def create_video_thumbnail(video_id: float, *, body: VideosPicturesRequest | VideosPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideosPicturesRequest` | `vimeo/models/videos_pictures_request.py` |
| `VideosPicturesRequestDict` | `vimeo/models/videos_pictures_request.py` |
| `Picture` | `vimeo/models/picture.py` |

### client.videos_thumbnails.create_video_thumbnail_alt1

- **Route**: `POST /channels/{channel_id}/videos/{video_id}/pictures`
- **Signature**: `def create_video_thumbnail_alt1(channel_id: float, video_id: float, *, body: ChannelsVideosPicturesRequest | ChannelsVideosPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChannelsVideosPicturesRequest` | `vimeo/models/channels_videos_pictures_request.py` |
| `ChannelsVideosPicturesRequestDict` | `vimeo/models/channels_videos_pictures_request.py` |
| `Picture` | `vimeo/models/picture.py` |

### client.videos_thumbnails.delete_video_thumbnail

- **Route**: `DELETE /videos/{video_id}/pictures/{picture_id}`
- **Signature**: `def delete_video_thumbnail(picture_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `picture_id`, `video_id`
- **Params**: `picture_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.videos_thumbnails.edit_video_thumbnail

- **Route**: `PATCH /videos/{video_id}/pictures/{picture_id}`
- **Signature**: `def edit_video_thumbnail(picture_id: float, video_id: float, *, body: VideosPicturesRequest1 | VideosPicturesRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `picture_id`, `video_id`
- **Params**: `picture_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideosPicturesRequest1` | `vimeo/models/videos_pictures_request1.py` |
| `VideosPicturesRequest1Dict` | `vimeo/models/videos_pictures_request1.py` |
| `Picture` | `vimeo/models/picture.py` |

### client.videos_thumbnails.get_video_thumbnail

- **Route**: `GET /videos/{video_id}/pictures/{picture_id}`
- **Signature**: `def get_video_thumbnail(picture_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `picture_id`, `video_id`
- **Params**: `picture_id` — path · `video_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |

### client.videos_thumbnails.get_video_thumbnails

- **Route**: `GET /videos/{video_id}/pictures`
- **Signature**: `def get_video_thumbnails(video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |

### client.videos_thumbnails.get_video_thumbnails_alt1

- **Route**: `GET /channels/{channel_id}/videos/{video_id}/pictures`
- **Signature**: `def get_video_thumbnails_alt1(channel_id: float, video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |

