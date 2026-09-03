<!-- Generated file — do not edit; regenerated with the SDK. -->

# CategoriesVideos — operations

Accessor: `client.categories_videos` · Source: `vimeo_api/apis/categories_videos.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.categories_videos.check_category_for_video

- **Route**: `GET /categories/{category}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_category_for_video(category: str, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`, `video_id`
- **Params**: `category` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, CheckCategoryForVideoErrorBody]`
- **Error**: `CheckCategoryForVideoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |
| `CheckCategoryForVideoErrorBody` | `vimeo_api/errors/check_category_for_video_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.categories_videos.get_category_videos

- **Route**: `GET /categories/{category}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_category_videos(category: str, *, direction: DirectionOrStr | None = None, filter: FilterOrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort6OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`
- **Params**: `category` — path · `direction` — query · `filter` — query · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetCategoryVideosErrorBody]`
- **Error**: `GetCategoryVideosErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `FilterOrStr` | `vimeo_api/models/enums/filter.py` |
| `Sort6OrStr` | `vimeo_api/models/enums/sort6.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `GetCategoryVideosErrorBody` | `vimeo_api/errors/get_category_videos_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.categories_videos.get_video_categories

- **Route**: `GET /videos/{video_id}/categories`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_video_categories(video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `CategoryConnection`
- **Returns (raw)**: `ApiResult[CategoryConnection, GetVideoCategoriesErrorBody]`
- **Error**: `GetVideoCategoriesErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CategoryConnection` | `vimeo_api/models/category_connection.py` |
| `GetVideoCategoriesErrorBody` | `vimeo_api/errors/get_video_categories_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.categories_videos.suggest_video_category

- **Route**: `PUT /videos/{video_id}/categories`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def suggest_video_category(video_id: float, body: VideosCategoriesRequest | VideosCategoriesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `body`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Category`
- **Returns (raw)**: `ApiResult[Category, SuggestVideoCategoryErrorBody]`
- **Error**: `SuggestVideoCategoryErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosCategoriesRequest` | `vimeo_api/models/videos_categories_request.py` |
| `VideosCategoriesRequestDict` | `vimeo_api/models/videos_categories_request.py` |
| `Category` | `vimeo_api/models/category.py` |
| `SuggestVideoCategoryErrorBody` | `vimeo_api/errors/suggest_video_category_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

