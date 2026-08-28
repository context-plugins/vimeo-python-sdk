<!-- Generated file — do not edit; regenerated with the SDK. -->

# ShowcasesShowcaseVideos — operations

Accessor: `client.showcases_showcase_videos` · Source: `vimeo/apis/showcases_showcase_videos.py` · 16 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.showcases_showcase_videos.add_video_to_showcase

- **Route**: `PUT /users/{user_id}/albums/{album_id}/videos/{video_id}`
- **Signature**: `def add_video_to_showcase(album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`, `video_id`
- **Params**: `album_id` — path · `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideoToShowcaseErrorBody]`
- **Error**: `AddVideoToShowcaseErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddVideoToShowcaseErrorBody` | `vimeo/errors/add_video_to_showcase_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.add_video_to_showcase_alt2

- **Route**: `PUT /me/albums/{album_id}/videos/{video_id}`
- **Signature**: `def add_video_to_showcase_alt2(album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `video_id`
- **Params**: `album_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideoToShowcaseAlt2ErrorBody]`
- **Error**: `AddVideoToShowcaseAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddVideoToShowcaseAlt2ErrorBody` | `vimeo/errors/add_video_to_showcase_alt2_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.get_available_showcase_videos

- **Route**: `GET /albums/{album_id}/available_videos`
- **Signature**: `def get_available_showcase_videos(album_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`
- **Params**: `album_id` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetAvailableShowcaseVideosErrorBody]`
- **Error**: `GetAvailableShowcaseVideosErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Sort2OrStr` | `vimeo/models/enums/sort2.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |
| `GetAvailableShowcaseVideosErrorBody` | `vimeo/errors/get_available_showcase_videos_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.get_available_video_showcases

- **Route**: `GET /videos/{video_id}/available_albums`
- **Signature**: `def get_available_video_showcases(video_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort74OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `AlbumConnection`
- **Returns (raw)**: `ApiResult[AlbumConnection, GetAvailableVideoShowcasesErrorBody]`
- **Error**: `GetAvailableVideoShowcasesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Sort74OrStr` | `vimeo/models/enums/sort74.py` |
| `AlbumConnection` | `vimeo/models/album_connection.py` |
| `GetAvailableVideoShowcasesErrorBody` | `vimeo/errors/get_available_video_showcases_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.showcases_showcase_videos.get_showcase_video

- **Route**: `GET /users/{user_id}/albums/{album_id}/videos/{video_id}`
- **Signature**: `def get_showcase_video(album_id: float, user_id: float, video_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`, `video_id`
- **Params**: `album_id` — path · `user_id` — path · `video_id` — path · `password` — query
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, GetShowcaseVideoErrorBody]`
- **Error**: `GetShowcaseVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo/models/video.py` |
| `GetShowcaseVideoErrorBody` | `vimeo/errors/get_showcase_video_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.get_showcase_video_alt2

- **Route**: `GET /me/albums/{album_id}/videos/{video_id}`
- **Signature**: `def get_showcase_video_alt2(album_id: float, video_id: float, *, password: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `video_id`
- **Params**: `album_id` — path · `video_id` — path · `password` — query
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, GetShowcaseVideoAlt2ErrorBody]`
- **Error**: `GetShowcaseVideoAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo/models/video.py` |
| `GetShowcaseVideoAlt2ErrorBody` | `vimeo/errors/get_showcase_video_alt2_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.get_showcase_videos

- **Route**: `GET /users/{user_id}/albums/{album_id}/videos`
- **Signature**: `def get_showcase_videos(album_id: float, user_id: float, *, containing_uri: str | None = None, direction: DirectionOrStr | None = None, filter: Filter10OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, password: str | None = None, per_page: float | None = None, query: str | None = None, sort: Sort21OrStr | None = None, weak_search: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`
- **Params**: `album_id` — path · `user_id` — path · `containing_uri` — query · `direction` — query · `filter` — query · `filter_embeddable` — query · `page` — query · `password` — query · `per_page` — query · `query` — query · `sort` — query · `weak_search` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetShowcaseVideosErrorBody]`
- **Error**: `GetShowcaseVideosErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter10OrStr` | `vimeo/models/enums/filter10.py` |
| `Sort21OrStr` | `vimeo/models/enums/sort21.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |
| `GetShowcaseVideosErrorBody` | `vimeo/errors/get_showcase_videos_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.get_showcase_videos_alt2

- **Route**: `GET /me/albums/{album_id}/videos`
- **Signature**: `def get_showcase_videos_alt2(album_id: float, *, containing_uri: str | None = None, direction: DirectionOrStr | None = None, filter: Filter10OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, password: str | None = None, per_page: float | None = None, query: str | None = None, sort: Sort21OrStr | None = None, weak_search: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`
- **Params**: `album_id` — path · `containing_uri` — query · `direction` — query · `filter` — query · `filter_embeddable` — query · `page` — query · `password` — query · `per_page` — query · `query` — query · `sort` — query · `weak_search` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetShowcaseVideosAlt2ErrorBody]`
- **Error**: `GetShowcaseVideosAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter10OrStr` | `vimeo/models/enums/filter10.py` |
| `Sort21OrStr` | `vimeo/models/enums/sort21.py` |
| `VideoConnection` | `vimeo/models/video_connection.py` |
| `GetShowcaseVideosAlt2ErrorBody` | `vimeo/errors/get_showcase_videos_alt2_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.remove_video_from_showcase

- **Route**: `DELETE /users/{user_id}/albums/{album_id}/videos/{video_id}`
- **Signature**: `def remove_video_from_showcase(album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`, `video_id`
- **Params**: `album_id` — path · `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveVideoFromShowcaseErrorBody]`
- **Error**: `RemoveVideoFromShowcaseErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveVideoFromShowcaseErrorBody` | `vimeo/errors/remove_video_from_showcase_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.remove_video_from_showcase_alt2

- **Route**: `DELETE /me/albums/{album_id}/videos/{video_id}`
- **Signature**: `def remove_video_from_showcase_alt2(album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `video_id`
- **Params**: `album_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveVideoFromShowcaseAlt2ErrorBody]`
- **Error**: `RemoveVideoFromShowcaseAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveVideoFromShowcaseAlt2ErrorBody` | `vimeo/errors/remove_video_from_showcase_alt2_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.replace_videos_in_showcase

- **Route**: `PUT /users/{user_id}/albums/{album_id}/videos`
- **Signature**: `def replace_videos_in_showcase(album_id: float, user_id: float, body: UsersAlbumsVideosRequest | UsersAlbumsVideosRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`, `body`
- **Params**: `album_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, ReplaceVideosInShowcaseErrorBody]`
- **Error**: `ReplaceVideosInShowcaseErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersAlbumsVideosRequest` | `vimeo/models/users_albums_videos_request.py` |
| `UsersAlbumsVideosRequestDict` | `vimeo/models/users_albums_videos_request.py` |
| `ReplaceVideosInShowcaseErrorBody` | `vimeo/errors/replace_videos_in_showcase_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.replace_videos_in_showcase_alt2

- **Route**: `PUT /me/albums/{album_id}/videos`
- **Signature**: `def replace_videos_in_showcase_alt2(album_id: float, body: MeAlbumsVideosRequest | MeAlbumsVideosRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `body`
- **Params**: `album_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, ReplaceVideosInShowcaseAlt2ErrorBody]`
- **Error**: `ReplaceVideosInShowcaseAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeAlbumsVideosRequest` | `vimeo/models/me_albums_videos_request.py` |
| `MeAlbumsVideosRequestDict` | `vimeo/models/me_albums_videos_request.py` |
| `ReplaceVideosInShowcaseAlt2ErrorBody` | `vimeo/errors/replace_videos_in_showcase_alt2_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.showcases_showcase_videos.set_video_as_showcase_featured

- **Route**: `PATCH /users/{user_id}/albums/{album_id}/videos/{video_id}/set_featured_video`
- **Signature**: `def set_video_as_showcase_featured(album_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`, `video_id`
- **Params**: `album_id` — path · `user_id` — path · `video_id` — path
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, SetVideoAsShowcaseFeaturedErrorBody]`
- **Error**: `SetVideoAsShowcaseFeaturedErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Album` | `vimeo/models/album.py` |
| `SetVideoAsShowcaseFeaturedErrorBody` | `vimeo/errors/set_video_as_showcase_featured_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.showcases_showcase_videos.set_video_as_showcase_featured_alt2

- **Route**: `PATCH /me/albums/{album_id}/videos/{video_id}/set_featured_video`
- **Signature**: `def set_video_as_showcase_featured_alt2(album_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `video_id`
- **Params**: `album_id` — path · `video_id` — path
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, SetVideoAsShowcaseFeaturedAlt2ErrorBody]`
- **Error**: `SetVideoAsShowcaseFeaturedAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Album` | `vimeo/models/album.py` |
| `SetVideoAsShowcaseFeaturedAlt2ErrorBody` | `vimeo/errors/set_video_as_showcase_featured_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.showcases_showcase_videos.set_video_as_showcase_thumbnail

- **Route**: `POST /users/{user_id}/albums/{album_id}/videos/{video_id}/set_album_thumbnail`
- **Signature**: `def set_video_as_showcase_thumbnail(album_id: float, user_id: float, video_id: float, *, body: UsersAlbumsVideosVideoIdSetAlbumThumbnailRequest | UsersAlbumsVideosVideoIdSetAlbumThumbnailRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`, `video_id`
- **Params**: `album_id` — path · `user_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, SetVideoAsShowcaseThumbnailErrorBody]`
- **Error**: `SetVideoAsShowcaseThumbnailErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersAlbumsVideosVideoIdSetAlbumThumbnailRequest` | `vimeo/models/users_albums_videos_video_id_set_album_thumbnail_request.py` |
| `UsersAlbumsVideosVideoIdSetAlbumThumbnailRequestDict` | `vimeo/models/users_albums_videos_video_id_set_album_thumbnail_request.py` |
| `Album` | `vimeo/models/album.py` |
| `SetVideoAsShowcaseThumbnailErrorBody` | `vimeo/errors/set_video_as_showcase_thumbnail_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.showcases_showcase_videos.set_video_as_showcase_thumbnail_alt2

- **Route**: `POST /me/albums/{album_id}/videos/{video_id}/set_album_thumbnail`
- **Signature**: `def set_video_as_showcase_thumbnail_alt2(album_id: float, video_id: float, *, body: MeAlbumsVideosSetAlbumThumbnailRequest | MeAlbumsVideosSetAlbumThumbnailRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `video_id`
- **Params**: `album_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, SetVideoAsShowcaseThumbnailAlt2ErrorBody]`
- **Error**: `SetVideoAsShowcaseThumbnailAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeAlbumsVideosSetAlbumThumbnailRequest` | `vimeo/models/me_albums_videos_set_album_thumbnail_request.py` |
| `MeAlbumsVideosSetAlbumThumbnailRequestDict` | `vimeo/models/me_albums_videos_set_album_thumbnail_request.py` |
| `Album` | `vimeo/models/album.py` |
| `SetVideoAsShowcaseThumbnailAlt2ErrorBody` | `vimeo/errors/set_video_as_showcase_thumbnail_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

