<!-- Generated file — do not edit; regenerated with the SDK. -->

# FoldersVideos — operations

Accessor: `client.folders_videos` · Source: `vimeo_api/apis/folders_videos.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.folders_videos.add_video_to_project

- **Route**: `PUT /users/{user_id}/projects/{project_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_video_to_project(project_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `user_id`, `video_id`
- **Params**: `project_id` — path · `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideoToProjectErrorBody]`
- **Error**: `AddVideoToProjectErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddVideoToProjectErrorBody` | `vimeo_api/errors/add_video_to_project_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_videos.add_video_to_project_alt1

- **Route**: `PUT /me/projects/{project_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_video_to_project_alt1(project_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `video_id`
- **Params**: `project_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideoToProjectAlt1ErrorBody]`
- **Error**: `AddVideoToProjectAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddVideoToProjectAlt1ErrorBody` | `vimeo_api/errors/add_video_to_project_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_videos.add_videos_to_project

- **Route**: `PUT /users/{user_id}/projects/{project_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_videos_to_project(project_id: float, user_id: float, body: UsersProjectsVideosRequest1 | UsersProjectsVideosRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `user_id`, `body`
- **Params**: `project_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideosToProjectErrorBody]`
- **Error**: `AddVideosToProjectErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersProjectsVideosRequest1` | `vimeo_api/models/users_projects_videos_request1.py` |
| `UsersProjectsVideosRequest1Dict` | `vimeo_api/models/users_projects_videos_request1.py` |
| `AddVideosToProjectErrorBody` | `vimeo_api/errors/add_videos_to_project_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_videos.add_videos_to_project_alt1

- **Route**: `PUT /me/projects/{project_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_videos_to_project_alt1(project_id: float, body: MeProjectsVideosRequest1 | MeProjectsVideosRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `body`
- **Params**: `project_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideosToProjectAlt1ErrorBody]`
- **Error**: `AddVideosToProjectAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeProjectsVideosRequest1` | `vimeo_api/models/me_projects_videos_request1.py` |
| `MeProjectsVideosRequest1Dict` | `vimeo_api/models/me_projects_videos_request1.py` |
| `AddVideosToProjectAlt1ErrorBody` | `vimeo_api/errors/add_videos_to_project_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_videos.get_project_videos

- **Route**: `GET /users/{user_id}/projects/{project_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_project_videos(project_id: float, user_id: float, *, direction: DirectionOrStr | None = None, filter_tag: str | None = None, filter_tag_all_of: str | None = None, filter_tag_exclude: str | None = None, include_subfolders: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, query_fields: str | None = None, sort: Sort37OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `user_id`
- **Params**: `project_id` — path · `user_id` — path · `direction` — query · `filter_tag` — query · `filter_tag_all_of` — query · `filter_tag_exclude` — query · `include_subfolders` — query · `page` — query · `per_page` — query · `query` — query · `query_fields` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetProjectVideosErrorBody]`
- **Error**: `GetProjectVideosErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort37OrStr` | `vimeo_api/models/enums/sort37.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `GetProjectVideosErrorBody` | `vimeo_api/errors/get_project_videos_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_videos.get_project_videos_alt1

- **Route**: `GET /me/projects/{project_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_project_videos_alt1(project_id: float, *, direction: DirectionOrStr | None = None, filter_tag: str | None = None, filter_tag_all_of: str | None = None, filter_tag_exclude: str | None = None, include_subfolders: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, query_fields: str | None = None, sort: Sort37OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `direction` — query · `filter_tag` — query · `filter_tag_all_of` — query · `filter_tag_exclude` — query · `include_subfolders` — query · `page` — query · `per_page` — query · `query` — query · `query_fields` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetProjectVideosAlt1ErrorBody]`
- **Error**: `GetProjectVideosAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort37OrStr` | `vimeo_api/models/enums/sort37.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `GetProjectVideosAlt1ErrorBody` | `vimeo_api/errors/get_project_videos_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_videos.remove_video_from_project

- **Route**: `DELETE /users/{user_id}/projects/{project_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def remove_video_from_project(project_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `user_id`, `video_id`
- **Params**: `project_id` — path · `user_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveVideoFromProjectErrorBody]`
- **Error**: `RemoveVideoFromProjectErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveVideoFromProjectErrorBody` | `vimeo_api/errors/remove_video_from_project_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_videos.remove_video_from_project_alt1

- **Route**: `DELETE /me/projects/{project_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def remove_video_from_project_alt1(project_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `video_id`
- **Params**: `project_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveVideoFromProjectAlt1ErrorBody]`
- **Error**: `RemoveVideoFromProjectAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RemoveVideoFromProjectAlt1ErrorBody` | `vimeo_api/errors/remove_video_from_project_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_videos.remove_videos_from_project

- **Route**: `DELETE /users/{user_id}/projects/{project_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def remove_videos_from_project(project_id: float, user_id: float, body: UsersProjectsVideosRequest | UsersProjectsVideosRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `user_id`, `body`
- **Params**: `project_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveVideosFromProjectErrorBody]`
- **Error**: `RemoveVideosFromProjectErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersProjectsVideosRequest` | `vimeo_api/models/users_projects_videos_request.py` |
| `UsersProjectsVideosRequestDict` | `vimeo_api/models/users_projects_videos_request.py` |
| `RemoveVideosFromProjectErrorBody` | `vimeo_api/errors/remove_videos_from_project_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_videos.remove_videos_from_project_alt1

- **Route**: `DELETE /me/projects/{project_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def remove_videos_from_project_alt1(project_id: float, body: MeProjectsVideosRequest | MeProjectsVideosRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `body`
- **Params**: `project_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveVideosFromProjectAlt1ErrorBody]`
- **Error**: `RemoveVideosFromProjectAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeProjectsVideosRequest` | `vimeo_api/models/me_projects_videos_request.py` |
| `MeProjectsVideosRequestDict` | `vimeo_api/models/me_projects_videos_request.py` |
| `RemoveVideosFromProjectAlt1ErrorBody` | `vimeo_api/errors/remove_videos_from_project_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

