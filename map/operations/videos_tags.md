<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosTags — operations

Accessor: `client.videos_tags` · Source: `vimeo_api/apis/videos_tags.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_tags.add_video_tag

- **Route**: `PUT /videos/{video_id}/tags/{word}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_video_tag(video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `word`
- **Params**: `video_id` — path · `word` — path
- **Returns (parsed)**: `TagModel`
- **Returns (raw)**: `ApiResult[TagModel, AddVideoTagErrorBody]`
- **Error**: `AddVideoTagErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TagModel` | `vimeo_api/models/tag_model.py` |
| `AddVideoTagErrorBody` | `vimeo_api/errors/add_video_tag_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_tags.add_video_tags

- **Route**: `PUT /videos/{video_id}/tags`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_video_tags(video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `list[TagModel]`
- **Returns (raw)**: `ApiResult[list[TagModel], AddVideoTagsErrorBody]`
- **Error**: `AddVideoTagsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TagModel` | `vimeo_api/models/tag_model.py` |
| `AddVideoTagsErrorBody` | `vimeo_api/errors/add_video_tags_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_tags.check_video_for_tag

- **Route**: `GET /videos/{video_id}/tags/{word}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_video_for_tag(video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `word`
- **Params**: `video_id` — path · `word` — path
- **Returns (parsed)**: `TagModel`
- **Returns (raw)**: `ApiResult[TagModel, CheckVideoForTagErrorBody]`
- **Error**: `CheckVideoForTagErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TagModel` | `vimeo_api/models/tag_model.py` |
| `CheckVideoForTagErrorBody` | `vimeo_api/errors/check_video_for_tag_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_tags.delete_video_tag

- **Route**: `DELETE /videos/{video_id}/tags/{word}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_video_tag(video_id: float, word: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `word`
- **Params**: `video_id` — path · `word` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoTagErrorBody]`
- **Error**: `DeleteVideoTagErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoTagErrorBody` | `vimeo_api/errors/delete_video_tag_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_tags.get_video_tags

- **Route**: `GET /videos/{video_id}/tags`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_video_tags(video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `TagConnection`
- **Returns (raw)**: `ApiResult[TagConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TagConnection` | `vimeo_api/models/tag_connection.py` |

### client.videos_tags.get_videos_with_tag

- **Route**: `GET /tags/{word}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_videos_with_tag(word: str, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort47OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `word`
- **Params**: `word` — path · `direction` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetVideosWithTagErrorBody]`
- **Error**: `GetVideosWithTagErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort47OrStr` | `vimeo_api/models/enums/sort47.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `GetVideosWithTagErrorBody` | `vimeo_api/errors/get_videos_with_tag_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

