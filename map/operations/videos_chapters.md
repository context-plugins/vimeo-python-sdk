<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosChapters — operations

Accessor: `client.videos_chapters` · Source: `vimeo_api/apis/videos_chapters.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_chapters.create_chapter

- **Route**: `POST /videos/{video_id}/chapters`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_chapter(video_id: float, *, body: VideosChaptersRequest | VideosChaptersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Chapter`
- **Returns (raw)**: `ApiResult[Chapter, CreateChapterErrorBody]`
- **Error**: `CreateChapterErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosChaptersRequest` | `vimeo_api/models/videos_chapters_request.py` |
| `VideosChaptersRequestDict` | `vimeo_api/models/videos_chapters_request.py` |
| `Chapter` | `vimeo_api/models/chapter.py` |
| `CreateChapterErrorBody` | `vimeo_api/errors/create_chapter_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.create_chapter_thumbnail_or_upload_link

- **Route**: `POST /videos/{video_id}/chapters/{chapter_id}/pictures`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_chapter_thumbnail_or_upload_link(chapter_id: float, video_id: float, *, body: VideosChaptersPicturesRequest | VideosChaptersPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chapter_id`, `video_id`
- **Params**: `chapter_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateChapterThumbnailOrUploadLinkErrorBody]`
- **Error**: `CreateChapterThumbnailOrUploadLinkErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosChaptersPicturesRequest` | `vimeo_api/models/videos_chapters_pictures_request.py` |
| `VideosChaptersPicturesRequestDict` | `vimeo_api/models/videos_chapters_pictures_request.py` |
| `Picture` | `vimeo_api/models/picture.py` |
| `CreateChapterThumbnailOrUploadLinkErrorBody` | `vimeo_api/errors/create_chapter_thumbnail_or_upload_link_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.create_unsaved_chapter_thumbnail_or_upload_link

- **Route**: `POST /videos/{video_id}/chapters/temporary/pictures`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_unsaved_chapter_thumbnail_or_upload_link(video_id: float, *, body: VideosChaptersTemporaryPicturesRequest | VideosChaptersTemporaryPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateUnsavedChapterThumbnailOrUploadLinkErrorBody]`
- **Error**: `CreateUnsavedChapterThumbnailOrUploadLinkErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosChaptersTemporaryPicturesRequest` | `vimeo_api/models/videos_chapters_temporary_pictures_request.py` |
| `VideosChaptersTemporaryPicturesRequestDict` | `vimeo_api/models/videos_chapters_temporary_pictures_request.py` |
| `Picture` | `vimeo_api/models/picture.py` |
| `CreateUnsavedChapterThumbnailOrUploadLinkErrorBody` | `vimeo_api/errors/create_unsaved_chapter_thumbnail_or_upload_link_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.delete_chapter

- **Route**: `DELETE /videos/{video_id}/chapters/{chapter_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_chapter(chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chapter_id`, `video_id`
- **Params**: `chapter_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteChapterErrorBody]`
- **Error**: `DeleteChapterErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteChapterErrorBody` | `vimeo_api/errors/delete_chapter_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.delete_chapter_thumbnail

- **Route**: `DELETE /videos/{video_id}/chapters/{chapter_id}/pictures/{uid}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_chapter_thumbnail(chapter_id: float, uid: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chapter_id`, `uid`, `video_id`
- **Params**: `chapter_id` — path · `uid` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteChapterThumbnailErrorBody]`
- **Error**: `DeleteChapterThumbnailErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteChapterThumbnailErrorBody` | `vimeo_api/errors/delete_chapter_thumbnail_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.edit_chapter

- **Route**: `PATCH /videos/{video_id}/chapters/{chapter_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_chapter(chapter_id: float, video_id: float, *, body: VideosChaptersRequest1 | VideosChaptersRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chapter_id`, `video_id`
- **Params**: `chapter_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Chapter`
- **Returns (raw)**: `ApiResult[Chapter, EditChapterErrorBody]`
- **Error**: `EditChapterErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosChaptersRequest1` | `vimeo_api/models/videos_chapters_request1.py` |
| `VideosChaptersRequest1Dict` | `vimeo_api/models/videos_chapters_request1.py` |
| `Chapter` | `vimeo_api/models/chapter.py` |
| `EditChapterErrorBody` | `vimeo_api/errors/edit_chapter_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.get_chapter

- **Route**: `GET /videos/{video_id}/chapters/{chapter_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_chapter(chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chapter_id`, `video_id`
- **Params**: `chapter_id` — path · `video_id` — path
- **Returns (parsed)**: `Chapter`
- **Returns (raw)**: `ApiResult[Chapter, GetChapterErrorBody]`
- **Error**: `GetChapterErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Chapter` | `vimeo_api/models/chapter.py` |
| `GetChapterErrorBody` | `vimeo_api/errors/get_chapter_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.get_chapter_thumbnail

- **Route**: `GET /videos/{video_id}/chapters/{chapter_id}/pictures/{uid}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_chapter_thumbnail(chapter_id: float, video_id: float, uid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chapter_id`, `video_id`, `uid`
- **Params**: `chapter_id` — path · `video_id` — path · `uid` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetChapterThumbnailErrorBody]`
- **Error**: `GetChapterThumbnailErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo_api/models/picture.py` |
| `GetChapterThumbnailErrorBody` | `vimeo_api/errors/get_chapter_thumbnail_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.get_chapter_thumbnails

- **Route**: `GET /videos/{video_id}/chapters/{chapter_id}/pictures`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_chapter_thumbnails(chapter_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chapter_id`, `video_id`
- **Params**: `chapter_id` — path · `video_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetChapterThumbnailsErrorBody]`
- **Error**: `GetChapterThumbnailsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo_api/models/picture.py` |
| `GetChapterThumbnailsErrorBody` | `vimeo_api/errors/get_chapter_thumbnails_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.get_chapters

- **Route**: `GET /videos/{video_id}/chapters`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_chapters(video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `ChapterConnection`
- **Returns (raw)**: `ApiResult[ChapterConnection, GetChaptersErrorBody]`
- **Error**: `GetChaptersErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChapterConnection` | `vimeo_api/models/chapter_connection.py` |
| `GetChaptersErrorBody` | `vimeo_api/errors/get_chapters_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.get_unsaved_chapter_thumbnail

- **Route**: `GET /videos/{video_id}/chapters/temporary/pictures/{uid}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_unsaved_chapter_thumbnail(video_id: float, uid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `uid`
- **Params**: `video_id` — path · `uid` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetUnsavedChapterThumbnailErrorBody]`
- **Error**: `GetUnsavedChapterThumbnailErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo_api/models/picture.py` |
| `GetUnsavedChapterThumbnailErrorBody` | `vimeo_api/errors/get_unsaved_chapter_thumbnail_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_chapters.set_chapter_thumbnail_active

- **Route**: `PATCH /videos/{video_id}/chapters/{chapter_id}/pictures/{uid}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def set_chapter_thumbnail_active(chapter_id: float, video_id: float, uid: str, *, body: VideosChaptersPicturesUidRequest | VideosChaptersPicturesUidRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chapter_id`, `video_id`, `uid`
- **Params**: `chapter_id` — path · `video_id` — path · `uid` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, SetChapterThumbnailActiveErrorBody]`
- **Error**: `SetChapterThumbnailActiveErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosChaptersPicturesUidRequest` | `vimeo_api/models/videos_chapters_pictures_uid_request.py` |
| `VideosChaptersPicturesUidRequestDict` | `vimeo_api/models/videos_chapters_pictures_uid_request.py` |
| `Picture` | `vimeo_api/models/picture.py` |
| `SetChapterThumbnailActiveErrorBody` | `vimeo_api/errors/set_chapter_thumbnail_active_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

