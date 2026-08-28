<!-- Generated file — do not edit; regenerated with the SDK. -->

# ShowcasesCustomShowcaseThumbnails — operations

Accessor: `client.showcases_custom_showcase_thumbnails` · Source: `vimeo/apis/showcases_custom_showcase_thumbnails.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.showcases_custom_showcase_thumbnails.create_showcase_custom_thumb

- **Route**: `POST /users/{user_id}/albums/{album_id}/custom_thumbnails`
- **Signature**: `def create_showcase_custom_thumb(album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`
- **Params**: `album_id` — path · `user_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateShowcaseCustomThumbErrorBody]`
- **Error**: `CreateShowcaseCustomThumbErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `CreateShowcaseCustomThumbErrorBody` | `vimeo/errors/create_showcase_custom_thumb_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_custom_showcase_thumbnails.delete_showcase_custom_thumbnail

- **Route**: `DELETE /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}`
- **Signature**: `def delete_showcase_custom_thumbnail(album_id: float, thumbnail_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `thumbnail_id`, `user_id`
- **Params**: `album_id` — path · `thumbnail_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteShowcaseCustomThumbnailErrorBody]`
- **Error**: `DeleteShowcaseCustomThumbnailErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteShowcaseCustomThumbnailErrorBody` | `vimeo/errors/delete_showcase_custom_thumbnail_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_custom_showcase_thumbnails.get_showcase_custom_thumbnail

- **Route**: `GET /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}`
- **Signature**: `def get_showcase_custom_thumbnail(album_id: float, thumbnail_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `thumbnail_id`, `user_id`
- **Params**: `album_id` — path · `thumbnail_id` — path · `user_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetShowcaseCustomThumbnailErrorBody]`
- **Error**: `GetShowcaseCustomThumbnailErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `GetShowcaseCustomThumbnailErrorBody` | `vimeo/errors/get_showcase_custom_thumbnail_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_custom_showcase_thumbnails.get_showcase_custom_thumbs

- **Route**: `GET /users/{user_id}/albums/{album_id}/custom_thumbnails`
- **Signature**: `def get_showcase_custom_thumbs(album_id: float, user_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`
- **Params**: `album_id` — path · `user_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, GetShowcaseCustomThumbsErrorBody]`
- **Error**: `GetShowcaseCustomThumbsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |
| `GetShowcaseCustomThumbsErrorBody` | `vimeo/errors/get_showcase_custom_thumbs_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_custom_showcase_thumbnails.replace_showcase_custom_thumb

- **Route**: `PATCH /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}`
- **Signature**: `def replace_showcase_custom_thumb(album_id: float, thumbnail_id: float, user_id: float, *, body: UsersAlbumsCustomThumbnailsThumbnailIdRequest | UsersAlbumsCustomThumbnailsThumbnailIdRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `thumbnail_id`, `user_id`
- **Params**: `album_id` — path · `thumbnail_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, ReplaceShowcaseCustomThumbErrorBody]`
- **Error**: `ReplaceShowcaseCustomThumbErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersAlbumsCustomThumbnailsThumbnailIdRequest` | `vimeo/models/users_albums_custom_thumbnails_thumbnail_id_request.py` |
| `UsersAlbumsCustomThumbnailsThumbnailIdRequestDict` | `vimeo/models/users_albums_custom_thumbnails_thumbnail_id_request.py` |
| `Picture` | `vimeo/models/picture.py` |
| `ReplaceShowcaseCustomThumbErrorBody` | `vimeo/errors/replace_showcase_custom_thumb_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

