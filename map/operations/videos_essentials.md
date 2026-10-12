<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosEssentials — operations

Accessor: `client.videos_essentials` · Source: `vimeo_api/apis/videos_essentials.py` · 15 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_essentials.check_if_user_owns_video

- **Route**: `GET /users/{user_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_if_user_owns_video(user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, CheckIfUserOwnsVideoErrorBody]`
- **Error**: `CheckIfUserOwnsVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |
| `CheckIfUserOwnsVideoErrorBody` | `vimeo_api/errors/check_if_user_owns_video_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_essentials.check_if_user_owns_video_alt1

- **Route**: `GET /me/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_if_user_owns_video_alt1(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, CheckIfUserOwnsVideoAlt1ErrorBody]`
- **Error**: `CheckIfUserOwnsVideoAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |
| `CheckIfUserOwnsVideoAlt1ErrorBody` | `vimeo_api/errors/check_if_user_owns_video_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_essentials.copy_video

- **Route**: `POST /users/{user_id}/videos/{video_id}/copy`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def copy_video(user_id: float, video_id: float, *, body: UsersVideosCopyRequest | UsersVideosCopyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, CopyVideoErrorBody]`
- **Error**: `CopyVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersVideosCopyRequest` | `vimeo_api/models/users_videos_copy_request.py` |
| `UsersVideosCopyRequestDict` | `vimeo_api/models/users_videos_copy_request.py` |
| `Video` | `vimeo_api/models/video.py` |
| `CopyVideoErrorBody` | `vimeo_api/errors/copy_video_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_essentials.copy_video_alt2

- **Route**: `POST /me/videos/{video_id}/copy`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def copy_video_alt2(video_id: float, *, body: MeVideosCopyRequest | MeVideosCopyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, CopyVideoAlt2ErrorBody]`
- **Error**: `CopyVideoAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeVideosCopyRequest` | `vimeo_api/models/me_videos_copy_request.py` |
| `MeVideosCopyRequestDict` | `vimeo_api/models/me_videos_copy_request.py` |
| `Video` | `vimeo_api/models/video.py` |
| `CopyVideoAlt2ErrorBody` | `vimeo_api/errors/copy_video_alt2_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_essentials.delete_video

- **Route**: `DELETE /videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_video(video_id: float, *, body: VideosRequest | VideosRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoErrorBody]`
- **Error**: `DeleteVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosRequest` | `vimeo_api/models/videos_request.py` |
| `VideosRequestDict` | `vimeo_api/models/videos_request.py` |
| `DeleteVideoErrorBody` | `vimeo_api/errors/delete_video_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_essentials.delete_videos

- **Route**: `DELETE /users/{user_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_videos(user_id: float, uris: str, *, body: UsersVideosRequest | UsersVideosRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `uris`
- **Params**: `user_id` — path · `uris` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideosErrorBody]`
- **Error**: `DeleteVideosErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersVideosRequest` | `vimeo_api/models/users_videos_request.py` |
| `UsersVideosRequestDict` | `vimeo_api/models/users_videos_request.py` |
| `DeleteVideosErrorBody` | `vimeo_api/errors/delete_videos_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.videos_essentials.delete_videos_alt1

- **Route**: `DELETE /me/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_videos_alt1(uris: str, *, body: MeVideosRequest | MeVideosRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uris`
- **Params**: `uris` — query · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideosAlt1ErrorBody]`
- **Error**: `DeleteVideosAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeVideosRequest` | `vimeo_api/models/me_videos_request.py` |
| `MeVideosRequestDict` | `vimeo_api/models/me_videos_request.py` |
| `DeleteVideosAlt1ErrorBody` | `vimeo_api/errors/delete_videos_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.videos_essentials.edit_video

- **Route**: `PATCH /videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_video(video_id: float, body: VideosRequest1 | VideosRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `body`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, EditVideoErrorBody]`
- **Error**: `EditVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosRequest1` | `vimeo_api/models/videos_request1.py` |
| `VideosRequest1Dict` | `vimeo_api/models/videos_request1.py` |
| `Video` | `vimeo_api/models/video.py` |
| `EditVideoErrorBody` | `vimeo_api/errors/edit_video_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_essentials.get_appearances

- **Route**: `GET /users/{user_id}/appearances`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_appearances(user_id: float, *, direction: DirectionOrStr | None = None, filter_: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort15OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `filter_` — query `filter` · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetAppearancesErrorBody]`
- **Error**: `GetAppearancesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter3OrStr` | `vimeo_api/models/enums/filter3.py` |
| `Sort15OrStr` | `vimeo_api/models/enums/sort15.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `GetAppearancesErrorBody` | `vimeo_api/errors/get_appearances_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.videos_essentials.get_appearances_alt1

- **Route**: `GET /me/appearances`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_appearances_alt1(*, direction: DirectionOrStr | None = None, filter_: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort15OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter_` — query `filter` · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetAppearancesAlt1ErrorBody]`
- **Error**: `GetAppearancesAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter3OrStr` | `vimeo_api/models/enums/filter3.py` |
| `Sort15OrStr` | `vimeo_api/models/enums/sort15.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `GetAppearancesAlt1ErrorBody` | `vimeo_api/errors/get_appearances_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.videos_essentials.get_video

- **Route**: `GET /videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_video(video_id: float, *, time_links: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `time_links` — query
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, GetVideoErrorBody]`
- **Error**: `GetVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |
| `GetVideoErrorBody` | `vimeo_api/errors/get_video_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_essentials.get_videos

- **Route**: `GET /users/{user_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_videos(user_id: float, *, containing_uri: str | None = None, direction: DirectionOrStr | None = None, filter_: Filter22OrStr | None = None, filter_embeddable: bool | None = None, filter_playable: bool | None = None, filter_screen_recorded: bool | None = None, filter_tag: str | None = None, filter_tag_all_of: str | None = None, filter_tag_exclude: str | None = None, filter_uploader: float | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, query_fields: QueryFieldsOrStr | None = None, sort: Sort39OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `containing_uri` — query · `direction` — query · `filter_` — query `filter` · `filter_embeddable` — query · `filter_playable` — query · `filter_screen_recorded` — query · `filter_tag` — query · `filter_tag_all_of` — query · `filter_tag_exclude` — query · `filter_uploader` — query · `page` — query · `per_page` — query · `query` — query · `query_fields` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter22OrStr` | `vimeo_api/models/enums/filter22.py` |
| `QueryFieldsOrStr` | `vimeo_api/models/enums/query_fields.py` |
| `Sort39OrStr` | `vimeo_api/models/enums/sort39.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |

### client.videos_essentials.get_videos_alt1

- **Route**: `GET /me/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_videos_alt1(*, containing_uri: str | None = None, direction: DirectionOrStr | None = None, filter_: Filter22OrStr | None = None, filter_embeddable: bool | None = None, filter_playable: bool | None = None, filter_screen_recorded: bool | None = None, filter_tag: str | None = None, filter_tag_all_of: str | None = None, filter_tag_exclude: str | None = None, filter_uploader: float | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, query_fields: QueryFieldsOrStr | None = None, sort: Sort39OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `containing_uri` — query · `direction` — query · `filter_` — query `filter` · `filter_embeddable` — query · `filter_playable` — query · `filter_screen_recorded` — query · `filter_tag` — query · `filter_tag_all_of` — query · `filter_tag_exclude` — query · `filter_uploader` — query · `page` — query · `per_page` — query · `query` — query · `query_fields` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter22OrStr` | `vimeo_api/models/enums/filter22.py` |
| `QueryFieldsOrStr` | `vimeo_api/models/enums/query_fields.py` |
| `Sort39OrStr` | `vimeo_api/models/enums/sort39.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |

### client.videos_essentials.search_videos

- **Route**: `GET /videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def search_videos(*, direction: DirectionOrStr | None = None, filter_: Filter45OrStr | None = None, links: str | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort73OrStr | None = None, uris: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter_` — query `filter` · `links` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query · `uris` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, SearchVideosErrorBody]`
- **Error**: `SearchVideosErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 404] · `LegacyError` [503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter45OrStr` | `vimeo_api/models/enums/filter45.py` |
| `Sort73OrStr` | `vimeo_api/models/enums/sort73.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `SearchVideosErrorBody` | `vimeo_api/errors/search_videos_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_essentials.update_video_custom_metadata

- **Route**: `PUT /videos/{video_id}/custom_metadata`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def update_video_custom_metadata(video_id: float, *, body: VideosCustomMetadataRequest | VideosCustomMetadataRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `list[CustomMetadataValues]`
- **Returns (raw)**: `ApiResult[list[CustomMetadataValues], UpdateVideoCustomMetadataErrorBody]`
- **Error**: `UpdateVideoCustomMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `LegacyError` [401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosCustomMetadataRequest` | `vimeo_api/models/videos_custom_metadata_request.py` |
| `VideosCustomMetadataRequestDict` | `vimeo_api/models/videos_custom_metadata_request.py` |
| `CustomMetadataValues` | `vimeo_api/models/custom_metadata_values.py` |
| `UpdateVideoCustomMetadataErrorBody` | `vimeo_api/errors/update_video_custom_metadata_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

